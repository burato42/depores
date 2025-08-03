from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Sports(Base):
    __tablename__ = 'sports'

    sport_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    sport_name: Mapped[str]


class Leagues(Base):
    __tablename__ = 'leagues'

    league_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    league_name: Mapped[str]
    sport_id: Mapped[int] = mapped_column(ForeignKey('sports.sport_id'))


class Teams(Base):
    __tablename__ = 'teams'

    team_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    team_name: Mapped[str]
    league_id: Mapped[int] = mapped_column(ForeignKey('leagues.league_id'))


class Players(Base):
    __tablename__ = 'players'

    player_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    player_name: Mapped[str]
    player_position: Mapped[str]
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.team_id'))
