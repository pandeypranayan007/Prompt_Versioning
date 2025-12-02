from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, create_engine, select
from contextlib
from .models import Prompt, Experiment, Evaluation
from .core.config import settings
import uuid

engine = create_engine(settings.DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI(title="PromptDeck Backend")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# === Prompt Endpoints ===
@app.post("/prompts/")
def create_prompt(prompt: Prompt, session: Session = Depends(get_session)):
    session.add(prompt)
    session.commit()
    session.refresh(prompt)
    return prompt

@app.get("/prompts/{name}/latest")
def get_latest_prompt(name: str, session: Session = Depends(get_session)):
    stmt = select(Prompt).where(Prompt.name == name).order_by(Prompt.version.desc())
    prompt = session.exec(stmt).first()
    if not prompt:
        raise HTTPException(404, "Prompt not found")
    return prompt

# === Experiment & Logging ===
@app.post("/log")
async def log_completion(payload: dict):
    # Called from SDK on every LLM completion
    eval_record = Evaluation(**payload)
    with Session(engine) as session:
        session.add(eval_record)
        session.commit()
    return {"status": "logged"}