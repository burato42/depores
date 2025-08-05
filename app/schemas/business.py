from pydantic import BaseModel


class MixConfig:
    class Config:
        from_attributes = True


class SportCreate(BaseModel):
    name: str


class Sport(SportCreate, MixConfig):
    id: int


class LeagueCreate(BaseModel):
    name: str
    sport_id: int


class League(LeagueCreate, MixConfig):
    id: int


class TeamCreate(BaseModel):
    name: str
    league_id: int


class Team(TeamCreate, MixConfig):
    id: int


class PlayerCreate(BaseModel):
    name: str
    position: str | None
    team_id: int | None


class Player(PlayerCreate, MixConfig):
    id: int
