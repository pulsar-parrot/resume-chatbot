from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    PROJECT_NAME: str = "PydanticAI ChatBot"
    
    # AI Configuration
    AI_MODEL: str = "gpt-3.5-turbo"
    AI_MAX_TOKENS: int = 1024
    
    # In a real app, you would add more settings like:
    # - API keys
    # - Database URLs
    # - Auth settings
    
    class Config:
        env_file = ".env"

settings = Settings()