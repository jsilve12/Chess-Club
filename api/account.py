""" File to store API Endpoints related to accounts """
from fastapi import Depends, FastAPI


app = FastAPI()


@app.get('/navbar')
async def navbar():
    return {'token': 'token'}
