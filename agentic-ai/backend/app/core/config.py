import os

class Config:
    API_KEY = os.getenv("API_KEY")
    MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")
    OPENAI_API_URL = os.getenv("OPENAI_API_URL")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    DEBUG = os.getenv("DEBUG", "false").lower() in ("true", "1", "t")
