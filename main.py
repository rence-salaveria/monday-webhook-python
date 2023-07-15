from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Challenge(BaseModel):
    challenge: str


@app.post('/webhook/')
def webhook_handler(challenge: Challenge):
    return challenge
