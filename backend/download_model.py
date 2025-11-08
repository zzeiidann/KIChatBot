# download_model.py
import os
import requests
from pathlib import Path

def download_model():
    """Download model dari Hugging Face manual"""
    model_url = "https://huggingface.co/Arko007/skin-disease-detector-ai/resolve/main/skin_model.h5"
    model_dir = Path("app/models/weights")
    model_dir.mkdir(parents=True, exist_ok=True)
    model_path = model_dir / "skin_model.h5"
    
    if model_path.exists():
        print("✅ Model already exists")
        return str(model_path)
    
    print("📥 Downloading model...")
    try:
        response = requests.get(model_url, stream=True)
        response.raise_for_status()
        
        with open(model_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ Model downloaded: {model_path}")
        return str(model_path)
        
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return None

if __name__ == "__main__":
    download_model()