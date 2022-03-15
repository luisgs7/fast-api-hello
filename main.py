from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def hello(message: str):
    return {
        "message": message
    }


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "q": q
        }

