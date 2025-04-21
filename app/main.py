from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.config import settings

app = FastAPI(
    title="PydanticAI ChatBot",
    description="A simple chatbot using FastAPI and PydanticAI",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(chat_router, prefix="/api/chat", tags=["chat"])

@app.get("/")
async def root():
    return {"message": "Welcome to the PydanticAI ChatBot API"}