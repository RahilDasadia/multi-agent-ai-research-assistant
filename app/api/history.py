from fastapi import APIRouter
from app.db.session import SessionLocal
from app.db import models

router = APIRouter()


@router.get("/tasks")
def list_tasks():
    db = SessionLocal()
    tasks = db.query(models.Task).all()
    db.close()
    return tasks


@router.get("/runs")
def list_runs():
    db = SessionLocal()
    runs = db.query(models.Run).all()
    db.close()
    return runs


@router.get("/runs/{run_id}/messages")
def get_run_messages(run_id: int):
    db = SessionLocal()
    messages = db.query(models.AgentMessage).filter(
        models.AgentMessage.run_id == run_id
    ).all()
    db.close()
    return messages