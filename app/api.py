# app/api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from .summarizer import summarize_match
from .player_profile import get_player_profile
from .narrator import generate_narrative

app = FastAPI(title="Football Match Analysis API")

class MatchSummaryRequest(BaseModel):
    match_id: int

class MatchSummaryResponse(BaseModel):
    summary: str

class PlayerProfileRequest(BaseModel):
    match_id: int
    player_id: int

class PlayerProfileResponse(BaseModel):
    name: str
    passes: int
    finalizations: int
    dispossessions: int
    minutes_played: int

class NarrationRequest(BaseModel):
    match_id: int
    style: Optional[str] = "Formal"

class NarrationResponse(BaseModel):
    narrative: str

@app.post("/match_summary", response_model=MatchSummaryResponse)
def match_summary(request: MatchSummaryRequest):
    summary = summarize_match(request.match_id)
    if not summary:
        raise HTTPException(status_code=404, detail="Partida não encontrada ou erro na sumarização.")
    return {"summary": summary}

@app.post("/player_profile", response_model=PlayerProfileResponse)
def player_profile(request: PlayerProfileRequest):
    profile = get_player_profile(request.match_id, request.player_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Jogador não encontrado na partida.")
    return profile

@app.post("/narrate_match", response_model=NarrationResponse)
def narrate_match(request: NarrationRequest):
    narrative = generate_narrative(request.match_id, request.style)
    if not narrative:
        raise HTTPException(status_code=404, detail="Erro na geração da narrativa.")
    return {"narrative": narrative}
