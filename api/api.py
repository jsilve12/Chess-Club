""" File to store API Endpoints related to accounts """
from fastapi import Depends, FastAPI, APIRouter


router = APIRouter()


@router.get('/navbar')
async def navbar():
    return {'token': 'token'}
