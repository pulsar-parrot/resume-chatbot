# FastAPI PydanticAI ChatBot (Proof of Concept)

A simple chatbot application built with FastAPI and PydanticAI.

## Features

- Simple REST API with FastAPI
- AI-powered chat responses using PydanticAI
- In-memory conversation tracking (no database needed)

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-pydanticai-chatbot.git
cd fastapi-pydanticai-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

4. Access the API documentation:
```
http://localhost:8000/docs
```

## API Usage

### Chat Endpoint

```
POST /api/chat/
```

Request body:
```json
{
  "message": "Hello, how are you?",
  "conversation_id": null
}
```

Response:
```json
{
  "message": {
    "role": "assistant",
    "content": "I'm doing well, thank you for asking! How can I help you today?"
  },
  "conversation_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

## Project Structure

- `app/main.py`: FastAPI application setup
- `app/config.py`: Application settings
- `app/models/chat.py`: PydanticAI models for chat
- `app/api/chat.py`: Chat endpoint
- `app/services/chat_service.py`: Business logic for chat processing

## License

This project is licensed under the Apache License 2.0	
