from pydanticai import PydanticAI
from pydantic import BaseModel, Field
from typing import List, Optional

class Message(BaseModel):
    """Message model for chat conversations."""
    role: str = Field(..., description="The role of the message sender (user or assistant)")
    content: str = Field(..., description="The content of the message")

class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    message: str = Field(..., description="The user's message")
    conversation_id: Optional[str] = Field(None, description="The conversation ID if continuing a conversation")
    
class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    message: Message
    conversation_id: str

class ChatAssistantResponse(PydanticAI):
    """PydanticAI model to generate assistant responses."""
    response_content: str = Field(..., description="The content of the assistant's response")
    
    class Config:
        prompt_template = """
        You are a helpful assistant for a chatbot application.
        
        Previous conversation:
        {format_messages(message_history) if message_history else "No previous messages"}
        
        User: {user_message}
        
        Provide a helpful and concise response:
        """