from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse, Message
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Process a chat message and return a response."""
    try:
        response = await chat_service.process_message(
            user_message=request.message,
            conversation_id=request.conversation_id
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))