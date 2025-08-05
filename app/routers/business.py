from typing import List

from fastapi import APIRouter, HTTPException, status

from app.crud.business import crud_sport
from app.dependencies.core import DBSessionDep
from app.schemas.business import SportCreate, Sport


business_router = APIRouter(prefix="/api")


@business_router.get(
    "/sports",
    response_model=List[Sport],
)
async def get_sports(db: DBSessionDep):
    return await crud_sport.get_all(db)


@business_router.post("/sports", response_model=Sport)
async def add_sport(sport: SportCreate, db: DBSessionDep):
    current = await crud_sport.get_by_name(db, sport)
    if current.all():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Sport already exists"
        )
    return await crud_sport.add(db, sport)


@business_router.get("/sports/{sport_id}", response_model=Sport)
async def get_sport(sport_id: int, db: DBSessionDep):
    records = await crud_sport.get_by_id(db, sport_id)
    sport = records.first()
    if not sport:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Records is not found"
        )
    return sport
