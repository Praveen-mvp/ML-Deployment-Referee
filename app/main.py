from fastapi import FastAPI
from pydantic import BaseModel
from app.decision_engine import compare_deployment

app = FastAPI(title="ML Deployment Referee")

class DeploymentRequest(BaseModel):
    hardware: str
    deployment: str
    latency: str
    cost: str

@app.post("/compare")
def compare(req: DeploymentRequest):
    return compare_deployment(req.dict())

