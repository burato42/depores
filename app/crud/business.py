from app.models import Sports as SportDBModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.business import SportBase, Sport

class CRUDSport:

    async def add(self, db_session: AsyncSession, sport_obj: SportBase):
        db_sport = SportDBModel(**sport_obj.model_dump())

        db_session.add(db_sport)

        await db_session.commit()
        await db_session.refresh(db_sport)

        return db_sport

    async def get_all(self, db_session: AsyncSession):
        pass


crud_sport = CRUDSport()