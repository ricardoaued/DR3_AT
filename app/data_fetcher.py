# app/data_fetcher.py
from statsbombpy import sb
import json

def get_match_data(match_id: int):
    """
    Busca os dados brutos de uma partida usando o StatsBombPy.
    """
    try:
        match = sb.match(match_id)
        return match
    except Exception as e:
        print(f"Erro ao buscar dados da partida {match_id}: {e}")
        return None
