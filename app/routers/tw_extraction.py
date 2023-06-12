from typing import List

from fastapi import APIRouter, Depends, responses

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.tw_extraction import service

from datetime import datetime

#Endpoint
router = APIRouter(tags=["tw_extraction"])


@router.get("/tw_extraction/{search_id}")
async def get_tweet_by_searchId(id: int, db: Session = Depends(get_db)):

    #Combrobar que el usuario existe vía id
    result = await service.get_tweet_by_searchId(db, id);

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User not found"}
        )
        return response;

    else:
        return result;

#Get de los resultados de la semana
@router.get("/tw_extraction/{search_id}/{days}")
async def get_tweets_by_last_day(id: int, days: int, db: Session = Depends(get_db)):

    #Combrobar que el usuario existe vía id
    result = await service.get_tweets_by_day(db, id, days)

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User not found"}
        )
        return response;

    else:
        return result;


#Get de los resultados en base a unas fechas concretas
@router.get("/tw_extraction/{search_id}/{start_date}{end_date}")
async def get_tweets_by_last_day(id: int, start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):


    #Combrobar que el usuario existe vía id
    result = await service.get_tweets_by_date_range(db, id, start_date, end_date)

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User not found"}
        )
        return response;

    else:
        return result;