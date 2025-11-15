#!/bin/bash
# Script to run the complete KIChatBot application

echo " Starting KIChatBot Application..."
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Backend directory
BACKEND_DIR="/Users/mraffyzeidan/Learning/KIChatBot/backend"
FRONTEND_DIR="/Users/mraffyzeidan/Learning/KIChatBot/frontend"

# Function to start backend
start_backend() {
    echo -e "${BLUE}📦 Starting Backend Server...${NC}"
    cd "$BACKEND_DIR"
    source .venv/bin/activate
    python run.py &
    BACKEND_PID=$!
    echo -e "${GREEN} Backend started (PID: $BACKEND_PID)${NC}"
    echo ""
}

# Function to start frontend
start_frontend() {
    echo -e "${BLUE}🎨 Starting Frontend Server...${NC}"
    cd "$FRONTEND_DIR"
    npm start &
    FRONTEND_PID=$!
    echo -e "${GREEN} Frontend started (PID: $FRONTEND_PID)${NC}"
    echo ""
}

# Start both servers
start_backend
sleep 3
start_frontend

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}🎉 KIChatBot Application is Running!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${BLUE}🔗 Access Points:${NC}"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo -e "${BLUE}✨ Features Available:${NC}"
echo "   ✓ Login & Registration"
echo "   ✓ Skin Disease Prediction (AI Model)"
echo "   ✓ Product Catalog & Shopping Cart"
echo "   ✓ AI Chatbot Consultation"
echo ""
echo -e "${RED}Press Ctrl+C to stop both servers${NC}"
echo ""

# Wait for user interrupt
wait
