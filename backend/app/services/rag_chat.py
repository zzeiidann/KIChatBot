# app/services/rag_chat.py
from app.database.vector_db import search_products
import logging

logger = logging.getLogger(__name__)

def generate_response(user_message: str, conversation_history: list = None) -> str:
    """
    Generate response using RAG (Retrieval Augmented Generation)
    """
    try:
        # Search relevant products
        relevant_products = search_products(user_message, top_k=3)
        
        # Build context from products
        context = ""
        if relevant_products:
            context = "\n📦 Produk yang mungkin cocok:\n"
            for i, product in enumerate(relevant_products, 1):
                context += f"• {product['name']} - Rp {product['price']:,}\n"
                context += f"  {product['description']}\n"
        
        # Simple rule-based response
        user_msg_lower = user_message.lower()
        
        if any(word in user_msg_lower for word in ['kulit', 'skin', 'jerawat', 'acne', 'wajah', 'face']):
            if relevant_products:
                response = f"🔍 Berdasarkan keluhan Anda, saya menemukan produk-produk ini:{context}\n\n💡 Tips: Untuk diagnosis kulit yang lebih akurat, silakan gunakan fitur upload gambar pada aplikasi kami."
            else:
                response = "Saya memahami Anda bertanya tentang kulit. Untuk diagnosis kulit yang akurat, silakan gunakan fitur upload gambar pada aplikasi kami. Untuk produk perawatan kulit, kami memiliki berbagai pilihan yang tersedia."
        
        elif any(word in user_msg_lower for word in ['harga', 'price', 'mahal', 'murah', 'beli', 'buy']):
            if relevant_products:
                response = f"💰 Informasi harga produk:{context}"
            else:
                response = "Silakan sebutkan produk spesifik yang ingin Anda ketahui harganya, atau jelaskan kebutuhan kulit Anda."
        
        elif any(word in user_msg_lower for word in ['rekomendasi', 'recommend', 'sarankan', 'suggest']):
            if relevant_products:
                response = f"✨ Rekomendasi produk untuk Anda:{context}\n\nProduk-produk ini dipilih berdasarkan kebutuhan yang Anda sebutkan."
            else:
                response = "Bisa Anda jelaskan lebih detail tentang jenis kulit atau masalah kulit yang ingin diatasi? Saya akan berusaha memberikan rekomendasi yang tepat."
        
        else:
            response = f"Terima kasih atas pertanyaan Anda!{context}\n\nApakah ada hal spesifik tentang perawatan kulit atau produk yang ingin Anda ketahui?"
        
        logger.info(f"Generated response for: '{user_message}'")
        return response
        
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return "Maaf, terjadi error dalam memproses permintaan Anda. Silakan coba lagi atau gunakan fitur upload gambar untuk konsultasi kulit."