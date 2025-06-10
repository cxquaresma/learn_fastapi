from typing import Union
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI() # creates an instance of FastAPI

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/") #defines a GET endpoint at the root URL (endpoint = route = path)
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}") # defines a GET endpoint with a path parameter
async def read_item(item_id: int): # item_id is an integer path parameter
    return {"item_id": item_id} # returns a JSON response with the item_id

