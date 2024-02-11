from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Sports(BaseModel):
    name: str
    member: int


@app.post("/sports")
def member(sports: Sports):
    return {f'{sports.name}は{sports.member}人のスポーツです'}
