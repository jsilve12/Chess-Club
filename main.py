"""Origin for FastAPI."""

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from .api import api
from .website import base

app = FastAPI()
app.mount('/static', StaticFiles(directory='FastAPI/static'), name='static')


app.include_router(
    base.router,
    tags=['webpage']
)
app.include_router(
    api.router,
    prefix='/api/login',
    tags=['login']
)
