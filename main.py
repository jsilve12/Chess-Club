"""Origin for FastAPI."""

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from .api import api
from .website import base

app = FastAPI()
app.mount('/static', StaticFiles(directory='Chess_Club/static'), name='static')


app.include_router(
    base.router,
    tags=['webpage']
)
app.include_router(
    api.router,
    prefix='/api',
    tags=['api']
)
