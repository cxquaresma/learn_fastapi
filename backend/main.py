from typing import Union
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI() # creates an instance of FastAPI

# Order Matters: you need to define path users/me before users/{user_id}. 
# otherwise, FastAPI will not know which one to use when both paths match 
# and will think /me is a user_id.
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
