# app/database/vector_db.py
import numpy as np
from .connection import get_db
from sklearn.metrics.pairwise import cosine_similarity
import logging

logger = logging.getLogger(__name__)

# Simple text embedding function
def get_text_embedding(text: str) -> np.ndarray:
    """
    Simple text embedding menggunakan approach sederhana
    """
    if not text:
        return np.zeros(100)
    
    text = text.lower().strip()
    words = text.split()
    
    # Create simple embedding based on character frequencies
    embedding = np.zeros(100)
    
    for i, char in enumerate(text[:100]):  # Use first 100 characters
        embedding[i % 100] += ord(char) / 1000.0
    
    # Add word presence features
    skincare_keywords = {
        'kulit': 1.0, 'skin': 1.0, 'jerawat': 0.9, 'acne': 0.9, 
        'kering': 0.8, 'dry': 0.8, 'berminyak': 0.8, 'oily': 0.8,
        'sensitif': 0.7, 'sensitive': 0.7, 'pori': 0.6, 'pore': 0.6,
        'bekas': 0.5, 'scar': 0.5, 'merah': 0.5, 'redness': 0.5,
        'gatal': 0.4, 'itchy': 0.4, 'kulit': 0.3, 'face': 0.3
    }
    
    for word, weight in skincare_keywords.items():
        if word in text:
            embedding[len(embedding) - 1 - list(skincare_keywords.keys()).index(word) % 10] += weight
    
    # Normalize
    norm = np.linalg.norm(embedding)
    if norm > 0:
        embedding = embedding / norm
    
    return embedding

def search_products(query: str, top_k: int = 3):
    """
    Search products based on text similarity
    """
    try:
        db = get_db()
        cursor = db.cursor()
        
        # Get all products
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        
        # Convert to list of dicts
        product_dicts = []
        for product in products:
            product_dicts.append({
                'id': product[0],
                'name': product[1],
                'description': product[2],
                'price': product[3],
                'category': product[4],
                'image_url': product[5]
            })
        
        # Get query embedding
        query_embedding = get_text_embedding(query)
        
        # Calculate similarities dengan semua produk
        similarities = []
        for product in product_dicts:
            # Create product text representation
            product_text = f"{product['name']} {product['description']} {product['category']}"
            product_embedding = get_text_embedding(product_text)
            
            # Calculate cosine similarity
            similarity = cosine_similarity([query_embedding], [product_embedding])[0][0]
            similarities.append((product, similarity))
        
        # Sort by similarity dan ambil top_k
        similarities.sort(key=lambda x: x[1], reverse=True)
        top_results = [product for product, score in similarities[:top_k]]
        
        logger.info(f"Search found {len(top_results)} products for query: '{query}'")
        return top_results
        
    except Exception as e:
        logger.error(f"Search error: {e}")
        return []
    finally:
        if 'db' in locals():
            db.close()