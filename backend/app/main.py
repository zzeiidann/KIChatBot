# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Lifespan events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    try:
        # Initialize database (jika ada)
        try:
            from app.database.connection import init_db
            init_db()
            logger.info("✅ Database initialized")
        except ImportError:
            logger.info("ℹ️ No database configured")
        
        # Pre-load AI model
        from app.models.ai_model import skin_model
        skin_model._ensure_loaded()
        logger.info("✅ AI model pre-loaded")
        
    except Exception as e:
        logger.error(f"❌ Startup error: {e}")
    
    yield
    # Shutdown would go here

app = FastAPI(
    title="Skin Care ChatBot API", 
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Skin Care ChatBot API is running!",
        "endpoints": {
            "health": "/health",
            "predict": ["/predict", "/api/v1/predict"],
            "chat": ["/chat", "/api/v1/chat"],
            "routes": "/routes"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "skin-care-chatbot"}

# Import dan register routers
try:
    # Import routers
    from app.routes.predict import router as predict_router
    from app.routes.chat import router as chat_router
    
    # Register dengan prefix API v1
    app.include_router(predict_router, prefix="/api/v1", tags=["prediction"])
    app.include_router(chat_router, prefix="/api/v1", tags=["chat"])
    
    # Juga register tanpa prefix untuk compatibility
    app.include_router(predict_router, tags=["prediction-legacy"])
    app.include_router(chat_router, tags=["chat-legacy"])
    
    logger.info("✅ All routes loaded successfully")
    logger.info("📌 Available endpoints:")
    logger.info("   - POST /api/v1/predict")
    logger.info("   - POST /predict") 
    logger.info("   - POST /api/v1/chat")
    logger.info("   - POST /chat")
    
except Exception as e:
    logger.error(f"❌ Routes loading failed: {e}")
    raise e

# Debug endpoint untuk melihat semua routes
@app.get("/routes")
async def list_routes():
    routes = []
    for route in app.routes:
        if hasattr(route, "methods"):
            routes.append({
                "path": route.path,
                "name": route.name,
                "methods": list(route.methods)
            })
    return routes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)