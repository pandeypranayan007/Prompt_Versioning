import random
import os

def choose_prompt_variant(experiment_name: str) -> str:
    # In real app: read from Redis/DB
    variants = ["customer-support-v1", "customer-support-v2"]
    weights = [0.7, 0.3]
    return random.choices(variants, weights=weights)[0]

# Set in your middleware or load balancer
os.environ["PROMPTDECK_EXPERIMENT_ID"] = "exp-123"
os.environ["PROMPTDECK_PROMPT_NAME"] = choose_prompt_variant("support-tone")