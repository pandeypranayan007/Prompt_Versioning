from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid

class Prompt(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True, unique=True)
    version: int = Field(default=1)
    content: str
    tags: str = Field(default="[]")  # JSON string
    metadata: str = Field(default="{}")
    is_production: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user_id: str

class Experiment(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    prompt_variants: str  # JSON list of prompt names
    traffic_allocation: str  # JSON [0.7, 0.3]
    status: str = "running"  # running, paused, completed
    winner_prompt: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Evaluation(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    experiment_id: uuid.UUID
    prompt_name: str
    input: str
    output: str
    score: Optional[float] = None
    judge_feedback: Optional[str] = None
    latency_ms: int
    cost_usd: float
    created_at: datetime = Field(default_factory=datetime.utcnow)