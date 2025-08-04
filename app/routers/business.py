from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.business import crud_sport
from app.dependencies.core import DBSessionDep
from app.schemas.business import SportBase, Sport

business_router = APIRouter(prefix='/api/')


@business_router.post('/sports/', response_model=Sport)
async def add_sport(db: Annotated[AsyncSession, Depends(DBSessionDep)], sport: SportBase):
    return await crud_sport.add(db, sport)



@business_router.post('/sports/', response_model=List[Sport])
async def get_sports(db: Annotated[AsyncSession, Depends(DBSessionDep)]):
    return await crud_sport.get_all(db)
