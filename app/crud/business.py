from fastapi import HTTPException, status
from sqlalchemy import ScalarResult

from app.models.business import Sports as SportDBModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.schemas.business import SportCreate


class CRUDSport:
    async def add(
        self, db_session: AsyncSession, sport_obj: SportCreate
    ) -> SportDBModel:
        existing = await db_session.scalars(
            select(SportDBModel).where(SportDBModel.name == sport_obj.name)
        )
        # TODO This approach doesn't work properly
        # if existing:
        #     # TODO Move such exceptions to the route
        #     raise HTTPException(
        #         status_code=status.HTTP_409_CONFLICT, detail="Sport already exists"
        #     )

        db_sport = SportDBModel(name=sport_obj.name)
        db_session.add(db_sport)
        await db_session.commit()
        await db_session.refresh(db_sport)

        return db_sport

    async def get_all(self, db_session: AsyncSession) -> ScalarResult[SportDBModel]:
        return await db_session.scalars(select(SportDBModel))

    async def get_by_id(self, db_session: AsyncSession, sport_id: int) -> SportDBModel:
        records = await db_session.scalars(
            select(SportDBModel).where(SportDBModel.id == sport_id)
        )
        # TODO This approach doesn't work properly
        # if not records:
        #     # TODO Move such exceptions to the router
        #     raise HTTPException(
        #         status_code=status.HTTP_404_NOT_FOUND, detail="Records is not found"
        #     )
        return records.first()


crud_sport = CRUDSport()
