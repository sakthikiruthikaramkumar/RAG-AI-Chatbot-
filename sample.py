from fastapi import FastAPI
from pydantic import BaseModel
from main import prompt

app = FastAPI()

class CompareRequest(BaseModel):
    symptoms: str
    prescribe: str

@app.post("/compare")
async def comparison(req: CompareRequest):
    try:
        response = prompt(req.symptoms, req.prescribe)
        return {"status": "success", "result": response}
    except Exception as e:
        return {"status": "error", "message": str(e)}
