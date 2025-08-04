from pydantic import BaseModel


class SportBase(BaseModel):
    sport_name: str


class Sport(SportBase):
    sport_id: int

    class Config:
        from_attributes = True


class League(BaseModel):
    league_id: int
    league_name: str
    sport_id: int


class Teams(BaseModel):
    team_id: int
    team_name: int
    league_id: int


class Player(BaseModel):
    player_id: int
    player_name: str
    player_position: str | None
    team_id: int | None


