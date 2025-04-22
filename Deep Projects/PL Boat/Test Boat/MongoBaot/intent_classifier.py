# ===========================
# intent_classifier.py
# ===========================
def classify_query(query):
    q = query.lower()

    if "average" in q and "first innings" in q:
        return "avg_first_innings_score"
    if "seating capacity" in q or "capacity" in q:
        return "venue_capacity"
    if "boundary length" in q or "boundary width" in q:
        return "boundary_stats"
    if "pitch" in q:
        return "pitch_type"
    if "weather" in q and "current" in q:
        return "current_weather"
    if "matches played" in q and "last" in q and "months" in q:
        return "matches_last_n_months"
    if "spin bowling" in q:
        return "spin_rating"
    if "best score" in q and "t20" in q:
        return "highest_score_t20"
    if "lowest" in q and "odi" in q:
        return "lowest_odi_score"
    if "pace bowling" in q:
        return "pace_stats"
    if "who won the last" in q:
        return "last_match_winner"
    return "unknown"