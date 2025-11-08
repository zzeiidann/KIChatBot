# app/routes/chat.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging
import requests
import json

logger = logging.getLogger(__name__)

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    disease_info: Optional[dict] = None  # ✅ FIXED: Ubah ke Optional

class ChatResponse(BaseModel):
    success: bool
    response: str
    message: str = ""

# Konfigurasi Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral"  # atau "llama3"

# Cache sederhana untuk response cepat
QUICK_RESPONSES = {
    "produk": "Untuk {disease}, saya sarankan:\n\n✨ **Produk Perawatan:**\n• Sunscreen SPF 50+ (Skin Aqua, Biore)\n• Gentle cleanser (Cetaphil, Simple)\n• Pelembap non-comedogenic (Hada Labo, Wardah)\n• Spot treatment (tea tree oil)\n\n💡 **Brand Lokal Terjangkau:** Somethinc, Avoskin, Whitelab\n\n⚠️ Konsultasi dokter kulit untuk rekomendasi spesifik!",
    
    "obat": "Pengobatan {disease} tergantung tingkat keparahan:\n\n💊 **Opsi Umum:**\n• Krim topikal (benzoyl peroxide, retinoid)\n• Antibiotik oral (jika perlu)\n• Terapi laser/light (prosedur dokter)\n\n🩺 **PENTING:** Jangan self-medicate! Konsultasi dermatologist untuk treatment plan yang tepat.",
    
    "apa itu": "**{disease}** adalah kondisi kulit yang terdeteksi dengan akurasi {confidence}%.\n\n📊 Deteksi AI bersifat screening awal, bukan diagnosis medis.\n\n🏥 Untuk diagnosis pasti dan treatment plan, silakan konsultasi dengan dokter spesialis kulit (Sp.KK).",
    
    "penyebab": "Penyebab {disease} bisa beragam:\n\n🧬 Faktor genetik\n🌍 Lingkungan (polusi, cuaca)\n🍔 Diet dan lifestyle\n💧 Ketidakseimbangan hormon\n\n🔍 Dokter kulit dapat identifikasi penyebab spesifik melalui pemeriksaan menyeluruh.",
    
    "cegah": "Tips pencegahan {disease}:\n\n🛡️ **Perlindungan:**\n• Gunakan sunscreen setiap hari\n• Hindari iritan dan alergen\n• Jaga kebersihan kulit\n\n💪 **Gaya Hidup:**\n• Diet seimbang\n• Cukup tidur & kelola stress\n• Rutin periksa kulit\n\n⏰ Deteksi dini sangat penting!",
}

def get_quick_response(user_message: str, disease_info: dict) -> str:
    """Cari response cepat dari cache"""
    user_lower = user_message.lower()
    disease_name = disease_info.get('disease', 'kondisi kulit') if disease_info else 'kondisi kulit'
    confidence = f"{(disease_info.get('confidence', 0) * 100):.1f}%" if disease_info else "0%"
    
    for key, template in QUICK_RESPONSES.items():
        if key in user_lower:
            return template.format(disease=disease_name, confidence=confidence)
    return None

def get_ollama_response(user_message: str, disease_info: dict) -> str:
    """Get response from Ollama - Optimized for speed"""
    try:
        # ✅ Cek quick response dulu (instant!)
        quick_response = get_quick_response(user_message, disease_info)
        if quick_response:
            logger.info("⚡ Using quick response")
            return quick_response
            
        disease_name = disease_info.get('disease', 'kondisi kulit') if disease_info else 'kondisi kulit'
        confidence = disease_info.get('confidence', 0) * 100 if disease_info else 0
        
        # ✅ Prompt yang lebih baik
        prompt = f"""Kamu adalah asisten dermatologi AI. Jawab dengan SINGKAT dan INFORMATIF (max 4 kalimat).

Kondisi Terdeteksi: {disease_name}
Akurasi AI: {confidence:.1f}%
Pertanyaan User: {user_message}

Berikan jawaban praktis dalam Bahasa Indonesia dengan emoji yang sesuai. Selalu ingatkan untuk konsultasi dokter jika perlu:"""
        
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.3,
                "top_p": 0.7,
                "num_predict": 250,  # ✅ Slightly increased
                "repeat_penalty": 1.1
            }
        }
        
        logger.info("🤖 Calling Ollama...")
        response = requests.post(OLLAMA_URL, json=payload, timeout=20)  # ✅ Increased timeout
        response.raise_for_status()
        
        result = response.json()
        return result["response"].strip()
        
    except requests.exceptions.Timeout:
        logger.warning("⏱️ Ollama timeout")
        return "Maaf, respons sedang lambat. Silakan konsultasi langsung dengan dokter kulit untuk informasi akurat. 🏥"
    
    except requests.exceptions.ConnectionError:
        logger.error("🔴 Ollama not running")
        fallback = get_quick_response(user_message, disease_info)
        if fallback:
            return fallback
        return f"⚠️ AI sedang offline. Untuk informasi tentang {disease_name}, silakan konsultasi dengan dokter spesialis kulit."
    
    except Exception as e:
        logger.error(f"❌ Ollama error: {e}")
        fallback = get_quick_response(user_message, disease_info)
        if fallback:
            return fallback
        return f"Untuk informasi tentang {disease_name}, silakan konsultasi dengan dokter spesialis kulit. 🩺"

@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(chat_request: ChatRequest):
    """
    Chat endpoint untuk konsultasi AI tentang kondisi kulit
    """
    try:
        logger.info(f"💬 Chat request: {chat_request.message}")
        logger.info(f"🩺 Disease info: {chat_request.disease_info}")
        
        # ✅ Validasi input
        if not chat_request.message or len(chat_request.message.strip()) == 0:
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # ✅ Get AI response
        response_text = get_ollama_response(
            chat_request.message, 
            chat_request.disease_info or {}
        )
        
        logger.info(f"✅ Response generated: {response_text[:100]}...")
        
        return ChatResponse(
            success=True,
            response=response_text,
            message="AI response generated successfully"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Chat error: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Internal server error: {str(e)}"
        )