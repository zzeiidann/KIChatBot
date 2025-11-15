# app/services/rag_chat.py
from app.database.vector_db import search_products
import logging
import requests
import json

logger = logging.getLogger(__name__)

# Ollama Configuration
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.2:latest"  # Change this to your installed model

def call_ollama(prompt: str, context: str = "") -> str:
    """Call Ollama API for text generation"""
    try:
        full_prompt = f"""You are a skincare expert assistant for a skincare products e-commerce platform.

CONTEXT:
{context}

USER QUESTION: {prompt}

Provide a helpful, concise response in Indonesian language. If recommending products, mention them naturally in your response. Keep responses under 150 words."""

        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "max_tokens": 300
                }
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "").strip()
        else:
            logger.error(f"Ollama API error: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        logger.error("Cannot connect to Ollama. Make sure Ollama is running on localhost:11434")
        return None
    except Exception as e:
        logger.error(f"Error calling Ollama: {e}")
        return None

def generate_response(user_message: str, conversation_history: list = None) -> str:
    """
    Generate response using RAG (Retrieval Augmented Generation) with Ollama
    """
    try:
        # Load skincare knowledge base
        from app.database.products_data import SKINCARE_KNOWLEDGE
        
        # Search relevant products
        relevant_products = search_products(user_message, top_k=3)
        
        # Build comprehensive context from products and knowledge base
        product_context = f"SKINCARE KNOWLEDGE BASE:\n{SKINCARE_KNOWLEDGE}\n\n"
        
        if relevant_products:
            product_context += "RELEVANT PRODUCTS:\n"
            for product in relevant_products:
                product_context += f"- {product['name']} (Rp {product['price']:,})\n"
                product_context += f"  Description: {product['description']}\n"
                if product.get('ingredients'):
                    product_context += f"  Ingredients: {product['ingredients']}\n"
                if product.get('usage'):
                    product_context += f"  Usage: {product['usage']}\n"
                product_context += "\n"
        
        # Try to get response from Ollama
        ollama_response = call_ollama(user_message, product_context)
        
        if ollama_response:
            logger.info(f"Generated response using Ollama for: '{user_message}'")
            return ollama_response
        
        # Fallback to rule-based response if Ollama is not available
        logger.warning("Ollama not available, using fallback response")
        
        user_msg_lower = user_message.lower()
        
        if any(word in user_msg_lower for word in ['kulit', 'skin', 'jerawat', 'acne', 'wajah', 'face']):
            if relevant_products:
                products_text = "\n".join([f"- {p['name']} - Rp {p['price']:,}: {p['description']}" for p in relevant_products])
                response = f"Berdasarkan keluhan Anda, saya menemukan produk-produk ini:\n\n{products_text}\n\nTips: Untuk diagnosis kulit yang lebih akurat, silakan gunakan fitur upload gambar pada aplikasi kami."
            else:
                response = "Saya memahami Anda bertanya tentang kulit. Untuk diagnosis kulit yang akurat, silakan gunakan fitur upload gambar pada aplikasi kami. Untuk produk perawatan kulit, kami memiliki berbagai pilihan yang tersedia."
        
        elif any(word in user_msg_lower for word in ['harga', 'price', 'mahal', 'murah', 'beli', 'buy']):
            if relevant_products:
                products_text = "\n".join([f"- {p['name']} - Rp {p['price']:,}" for p in relevant_products])
                response = f"Informasi harga produk:\n\n{products_text}"
            else:
                response = "Silakan sebutkan produk spesifik yang ingin Anda ketahui harganya, atau jelaskan kebutuhan kulit Anda."
        
        elif any(word in user_msg_lower for word in ['rekomendasi', 'recommend', 'sarankan', 'suggest']):
            if relevant_products:
                products_text = "\n".join([f"- {p['name']} - Rp {p['price']:,}: {p['description']}" for p in relevant_products])
                response = f"Rekomendasi produk untuk Anda:\n\n{products_text}\n\nProduk-produk ini dipilih berdasarkan kebutuhan yang Anda sebutkan."
            else:
                response = "Bisa Anda jelaskan lebih detail tentang jenis kulit atau masalah kulit yang ingin diatasi? Saya akan berusaha memberikan rekomendasi yang tepat."
        
        else:
            if relevant_products:
                products_text = "\n".join([f"- {p['name']} - Rp {p['price']:,}" for p in relevant_products])
                response = f"Terima kasih atas pertanyaan Anda!\n\nProduk yang mungkin relevan:\n{products_text}\n\nApakah ada hal spesifik tentang perawatan kulit atau produk yang ingin Anda ketahui?"
            else:
                response = "Terima kasih atas pertanyaan Anda! Apakah ada hal spesifik tentang perawatan kulit atau produk yang ingin Anda ketahui?"
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return "Maaf, terjadi error dalam memproses permintaan Anda. Silakan coba lagi atau gunakan fitur upload gambar untuk konsultasi kulit."