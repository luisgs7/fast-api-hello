from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello(message: str):
    return {
        "message": message
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "q": q
        }