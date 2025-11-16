# app/services/rag_chat.py
from app.database.vector_db import search_products
import logging
import requests
import json

logger = logging.getLogger(__name__)

# Ollama Configuration
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.2:latest"  # Change this to your installed model

def call_ollama(prompt: str, context: str = "") -> dict:
    """Call Ollama API for text generation and return response with product references"""
    try:
        full_prompt = f"""You are a skincare expert assistant for a skincare products e-commerce platform.

CONTEXT:
{context}

USER QUESTION: {prompt}

Provide a helpful, concise response in Indonesian language. When recommending products:
1. Explain WHY each product is suitable for the user's condition
2. Mention the product name clearly
3. Highlight key benefits or ingredients
4. Keep total response under 200 words

Be conversational and helpful. If multiple products are available, recommend 2-3 best options."""

        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "max_tokens": 350
                }
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return {"response": result.get("response", "").strip(), "success": True}
        else:
            logger.error(f"Ollama API error: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        logger.error("Cannot connect to Ollama. Make sure Ollama is running on localhost:11434")
        return None
    except Exception as e:
        logger.error(f"Error calling Ollama: {e}")
        return None

def generate_response(user_message: str, conversation_history: list = None) -> dict:
    """
    Generate response using RAG (Retrieval Augmented Generation) with Ollama
    Returns: {
        "response": str (text response),
        "products": list (recommended products with full details)
    }
    """
    try:
        # Load skincare knowledge base
        from app.database.products_data import SKINCARE_KNOWLEDGE
        
        # Search relevant products (increase to 5 for better selection)
        relevant_products = search_products(user_message, top_k=5)
        
        # Build comprehensive context from products and knowledge base
        product_context = f"SKINCARE KNOWLEDGE BASE:\n{SKINCARE_KNOWLEDGE}\n\n"
        
        if relevant_products:
            product_context += "=== AVAILABLE PRODUCTS IN OUR STORE ===\n\n"
            for idx, product in enumerate(relevant_products, 1):
                product_context += f"{idx}. **{product['name']}** (Rp {product['price']:,})\n"
                product_context += f"   Category: {product.get('category', 'General')}\n"
                if product.get('for_conditions'):
                    product_context += f"   Best for: {', '.join(product['for_conditions'])}\n"
                product_context += f"   Description: {product['description']}\n"
                if product.get('ingredients'):
                    product_context += f"   Key Ingredients: {product['ingredients']}\n"
                if product.get('usage'):
                    product_context += f"   How to Use: {product['usage']}\n"
                product_context += "\n"
        
        # Try to get response from Ollama
        ollama_result = call_ollama(user_message, product_context)
        
        if ollama_result and ollama_result.get("success"):
            logger.info(f"Generated response using Ollama for: '{user_message}'")
            return {
                "response": ollama_result["response"],
                "products": relevant_products[:3]  # Return top 3 products
            }
        
        # Fallback to rule-based response if Ollama is not available
        logger.warning("Ollama not available, using fallback response")
        
        user_msg_lower = user_message.lower()
        
        if any(word in user_msg_lower for word in ['kulit', 'skin', 'jerawat', 'acne', 'wajah', 'face']):
            if relevant_products:
                products_text = "\n".join([f"- {p['name']} - Rp {p['price']:,}: {p['description'][:100]}..." for p in relevant_products[:3]])
                response = f"Berdasarkan keluhan Anda, saya menemukan produk-produk ini:\n\n{products_text}\n\nTips: Untuk diagnosis kulit yang lebih akurat, silakan gunakan fitur upload gambar pada aplikasi kami."
            else:
                response = "Saya memahami Anda bertanya tentang kulit. Untuk diagnosis kulit yang akurat, silakan gunakan fitur upload gambar pada aplikasi kami. Untuk produk perawatan kulit, kami memiliki berbagai pilihan yang tersedia."
        
        elif any(word in user_msg_lower for word in ['harga', 'price', 'mahal', 'murah', 'beli', 'buy']):
            if relevant_products:
                products_text = "\n".join([f"- {p['name']} - Rp {p['price']:,}" for p in relevant_products[:3]])
                response = f"Informasi harga produk:\n\n{products_text}"
            else:
                response = "Silakan sebutkan produk spesifik yang ingin Anda ketahui harganya, atau jelaskan kebutuhan kulit Anda."
        
        elif any(word in user_msg_lower for word in ['rekomendasi', 'recommend', 'sarankan', 'suggest']):
            if relevant_products:
                products_text = "\n".join([f"- {p['name']} - Rp {p['price']:,}: {p['description'][:100]}..." for p in relevant_products[:3]])
                response = f"Rekomendasi produk untuk Anda:\n\n{products_text}\n\nProduk-produk ini dipilih berdasarkan kebutuhan yang Anda sebutkan."
            else:
                response = "Bisa Anda jelaskan lebih detail tentang jenis kulit atau masalah kulit yang ingin diatasi? Saya akan berusaha memberikan rekomendasi yang tepat."
        
        else:
            if relevant_products:
                products_text = "\n".join([f"- {p['name']} - Rp {p['price']:,}" for p in relevant_products[:3]])
                response = f"Terima kasih atas pertanyaan Anda!\n\nProduk yang mungkin relevan:\n{products_text}\n\nApakah ada hal spesifik tentang perawatan kulit atau produk yang ingin Anda ketahui?"
            else:
                response = "Terima kasih atas pertanyaan Anda! Apakah ada hal spesifik tentang perawatan kulit atau produk yang ingin Anda ketahui?"
        
        return {
            "response": response,
            "products": relevant_products[:3] if relevant_products else []
        }
        
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return {
            "response": "Maaf, terjadi error dalam memproses permintaan Anda. Silakan coba lagi atau gunakan fitur upload gambar untuk konsultasi kulit.",
            "products": []
        }