# app/player_profile.py
from statsbombpy import sb

def get_player_profile(match_id: int, player_id: int) -> dict:
    match_events = sb.events(match_id)
    player_events = [event for event in match_events if event.get('player', {}).get('id') == player_id]
    if not player_events:
        return {}
    profile = {
        "name": player_events[0]['player']['name'],
        "passes": 0,
        "finalizations": 0,
        "dispossessions": 0,
        "minutes_played": 0
    }
    for event in player_events:
        event_type = event['type']['name']
        if event_type == 'Pass':
            profile["passes"] += 1
        elif event_type in ['Shot', 'Goal']:
            profile["finalizations"] += 1
        elif event_type == 'Tackle':
            profile["dispossessions"] += 1
    minutes = [event['minute'] for event in player_events if 'minute' in event]
    if minutes:
        profile["minutes_played"] = max(minutes) - min(minutes) + 1
    return profile
