""" Core Website Pages """
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os


router = APIRouter()
templates = Jinja2Templates(directory='Chess_Club/templates')


@router.get('/', response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router.get('/about', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse('about.html', {'request': request})


@router.get('/learning', response_class=HTMLResponse)
async def settings(request: Request):
    return templates.TemplateResponse('learning.html', {'request': request})


@router.get('/tournaments', response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse('tournaments.html', {'request': request})

@router.get('/calendar', response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse('calendar.html', {'request': request})
