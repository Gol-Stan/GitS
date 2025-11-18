from fastapi import FastAPI
import aioredis
import json


app = FastAPI()
redis = aioredis.from_url("redis://localhost:6379", decode_responses=True)

async def cache(key: str, ttl: int = 60):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            cached = await redis.get(key)
            if cached:
                return json.loads(cached)
            result = await func(*args, **kwargs)
            await redis.set(key, json.dumps(result), ex=ttl)
            return result
        return wrapper
    return decorator