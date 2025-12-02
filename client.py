import os
import httpx
import uuid
from .decorators import prompt

class PromptDeckClient:
    def __init__(self, api_key: str = None, base_url: str = "http://localhost:8000"):
        self.api_key = api_key or os.getenv("PROMPTDECK_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client(headers={"Authorization": f"Bearer {self.api_key}"})
        self.current_experiment = None

    def log_completion(
        self,
        prompt_name: str,
        input: str,
        output: str,
        latency_ms: int,
        cost_usd: float,
        experiment_id: str = None,
    ):
        payload = {
            "experiment_id": experiment_id or self.current_experiment,
            "prompt_name": prompt_name,
            "input": input,
            "output": output,
            "latency_ms": latency_ms,
            "cost_usd": cost_usd,
        }
        try:
            self.client.post(f"{self.base_url}/log", json=payload, timeout=5.0)
        except:
            pass  # fire and forget