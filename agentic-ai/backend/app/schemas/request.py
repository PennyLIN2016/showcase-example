from pydantic import BaseModel

class UserRequest(BaseModel):
    question: str

class AgentResponse(BaseModel):
    answer: str
    confidence: float
