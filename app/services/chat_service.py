import uuid
from typing import Dict, List, Optional
from app.models.chat import Message, ChatResponse, ChatAssistantResponse

class ChatService:
    """Service for processing chat messages."""
    
    def __init__(self):
        # In-memory store for conversations (would use a database in production)
        self.conversations: Dict[str, List[Message]] = {}
    
    async def process_message(
        self, 
        user_message: str, 
        conversation_id: Optional[str] = None
    ) -> ChatResponse:
        """Process a user message and return a response."""
        
        # Create new conversation if none exists
        if not conversation_id or conversation_id not in self.conversations:
            conversation_id = str(uuid.uuid4())
            self.conversations[conversation_id] = []
        
        # Add user message to conversation history
        user_message_obj = Message(role="user", content=user_message)
        self.conversations[conversation_id].append(user_message_obj)
        
        # Get conversation history
        message_history = self.conversations[conversation_id][:-1]  # All but the latest message
        
        # Generate response using PydanticAI
        assistant_response = ChatAssistantResponse.invoke(
            user_message=user_message,
            message_history=message_history,
            format_messages=lambda msgs: "\n".join([f"{m.role}: {m.content}" for m in msgs])
        )
        
        # Create response message
        assistant_message = Message(
            role="assistant",
            content=assistant_response.response_content
        )
        
        # Save to conversation history
        self.conversations[conversation_id].append(assistant_message)
        
        return ChatResponse(
            message=assistant_message,
            conversation_id=conversation_id
        )