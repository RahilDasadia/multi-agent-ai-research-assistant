from app.db.base import Base
from app.db.session import engine
from app.db import models
from fastapi import FastAPI
from app.orchestrator.engine import Orchestrator
from app.api.history import router as history_router
from fastapi.responses import StreamingResponse
from fastapi.responses import HTMLResponse
app = FastAPI(
    title="Multi-Agent System",
    description="Backend for Multi-Agent AI Platform",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(history_router)

# @app.get("/")
# def root():
#     return {"message": "Multi-Agent System is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/run")
def run_workflow(task: str):
    orchestrator = Orchestrator()
    result = orchestrator.run(task)
    return {"final_output": result}

@app.get("/stream")
def stream_run(task: str):

    orchestrator = Orchestrator()

    def generate():

        result = orchestrator.run(task)

        for char in result:
            yield char

    return StreamingResponse(generate(), media_type="text/event-stream")

@app.get("/", response_class=HTMLResponse)
def home():

    with open("app/frontend/index.html") as f:
        return f.read()