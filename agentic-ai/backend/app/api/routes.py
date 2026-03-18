from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.openai_client import OpenAIClient
from app.services.mcp_client import MCPClient

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        mcp_client = MCPClient()
        openai_client = OpenAIClient()

        # Send the question to the MCP server and get a response
        mcp_response = mcp_client.send_question(request.question)

        # Process the response with OpenAI
        openai_response = openai_client.get_response(mcp_response)

        return {"response": openai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))