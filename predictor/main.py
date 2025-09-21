from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict_market_value

app = FastAPI(title="Football Market Value Predictor API")

class PlayerData(BaseModel):
    player_name: str
    league: str
    position: str
    age: int
    matches: int
    goals: int
    assists: int

@app.post("/predict")
def predict(data: PlayerData):
    value = predict_market_value(
        player_name=data.player_name,
        league=data.league,
        position=data.position,
        age=data.age,
        matches=data.matches,
        goals=data.goals,
        assists=data.assists,
    )
    return {"predicted_value_million_eur": value}
