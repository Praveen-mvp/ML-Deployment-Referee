from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.decision_engine import compare_deployment

app = FastAPI(title="ML Deployment Referee")

# ✅ ADD CORS MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow browser requests
    allow_credentials=True,
    allow_methods=["*"],        # allow OPTIONS, POST, etc.
    allow_headers=["*"],
)

class DeploymentRequest(BaseModel):
    hardware: str
    deployment: str
    latency: str
    cost: str

@app.post("/compare")
def compare(req: DeploymentRequest):
    return compare_deployment(req.dict())
