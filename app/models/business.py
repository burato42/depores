from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Sports(Base):
    __tablename__ = 'sports'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]


class Leagues(Base):
    __tablename__ = 'leagues'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]
    sport_id: Mapped[int] = mapped_column(ForeignKey('sports.id'))


class Teams(Base):
    __tablename__ = 'teams'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]
    league_id: Mapped[int] = mapped_column(ForeignKey('leagues.id'))


class Players(Base):
    __tablename__ = 'players'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]
    position: Mapped[str]
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))
