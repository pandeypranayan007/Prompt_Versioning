import time
import openai
from functools import wraps
from .client import PromptDeckClient

client = PromptDeckClient()

def prompt(name: str, version: str = "latest"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Build prompt
            prompt_text = func(*args, **kwargs)

            start = time.time()
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt_text}],
                temperature=0.7,
            )
            latency_ms = int((time.time() - start) * 1000)
            output = response.choices[0].message.content
            cost_usd = response.usage.total_tokens * 0.00001  # rough estimate

            # Auto-detect experiment from env or header
            experiment_id = os.getenv("PROMPTDECK_EXPERIMENT_ID")

            client.log_completion(
                prompt_name=name,
                input=prompt_text,
                output=output,
                latency_ms=latency_ms,
                cost_usd=cost_usd,
                experiment_id=experiment_id,
            )

            return output
        return wrapper
    return decorator