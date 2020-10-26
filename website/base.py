""" Core Website Pages """
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os


app = APIRouter()
templates = Jinja2Templates(directory='Boilerplate/templates')


@app.get('/', response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/about', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse('about.html', {'request': request})


@app.get('/learning', response_class=HTMLResponse)
async def settings(request: Request):
    return templates.TemplateResponse('learning.html', {'request': request})


@app.get('/tournaments', response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse('tournaments.html', {'request': request})
