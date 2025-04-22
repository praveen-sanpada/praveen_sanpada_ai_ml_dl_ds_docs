# ===========================
# query_router.py
# ===========================
from mongo_handlers import *

def query_router(intent, query, venue_data):
    if intent == "avg_first_innings_score":
        return get_avg_first_innings_score(venue_data)
    if intent == "venue_capacity":
        return get_venue_capacity(venue_data)
    if intent == "boundary_stats":
        return get_boundary_stats(venue_data)
    if intent == "pitch_type":
        return get_pitch_info(venue_data)
    if intent == "current_weather":
        return get_current_weather(venue_data)
    if intent == "matches_last_n_months":
        return get_matches_last_n_months(venue_data, months=6)
    if intent == "spin_rating":
        return get_spin_rating(venue_data)
    if intent == "highest_score_t20":
        return get_highest_score(venue_data, "t20")
    if intent == "lowest_odi_score":
        return get_lowest_score(venue_data, "odi")
    if intent == "pace_stats":
        return get_pace_performance(venue_data)
    if intent == "last_match_winner":
        return get_last_match_winner(venue_data)
    return "❌ Sorry, I don't yet handle this intent."