from dotenv import load_dotenv
import os
from openai import OpenAI
import time
from openai import RateLimitError, APIError

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_batch(texts: list[str], model: str= "text-embedding-3-small", max_retries: int=5) -> list[list[float]]:
    for attempt in range(max_retries):
        try:
            response = client.embeddings.create(input=texts,model=model)
            return [item.embedding for item in response.data]
        except (RateLimitError, APIError) as e:
            wait_time = 2 ** attempt
            print(f"API error ({e}), retrying in {wait_time}s... attempt {attempt + 1}/ {max_retries}")
            time.sleep(wait_time)

    raise RuntimeError(f"failed to embed after {max_retries} attempts")