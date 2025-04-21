# ===========================
# mongo_handlers.py
# ===========================
from datetime import datetime, timedelta

def get_avg_first_innings_score(data, fmt="odi"):
    return f"Avg first innings score: {data.get(fmt, {}).get('sts', {}).get('1', {}).get('f', {}).get('as', 'N/A')}"

def get_venue_capacity(data):
    return f"Seating capacity: {data.get('vde', {}).get('cpt', 'N/A')}"

def get_boundary_stats(data):
    v = data.get('vde', {})
    return f"Boundary length: {v.get('blt')}m, width: {v.get('bwd')}m"

def get_pitch_info(data):
    p = data.get('pit', {})
    return f"Pitch: {p.get('pcd')}, Pace: {p.get('pbcd')}, Spin: {p.get('sbcd')}"

def get_current_weather(data):
    w = data.get('wth', {})
    return f"Weather: {w.get('wth')}, Temp: {w.get('tmp')}°C, Humidity: {w.get('hmd')}%"

def get_matches_last_n_months(data, months=6, fmt="odi"):
    from dateutil.parser import parse
    now = datetime.now()
    since = now - timedelta(days=30*months)
    all_matches = data.get(fmt, {}).get("mch", {})
    recent = [m for m in all_matches.values() if parse(m["sdt"]) >= since]
    return f"Matches in last {months} months: {len(recent)}"

def get_spin_rating(data):
    return f"Spin bowling condition: {data.get('pit', {}).get('sbcd', 'N/A')}"

def get_highest_score(data, fmt="t20"):
    stats = [data.get(fmt, {}).get("sts", {}).get(str(i), {}) for i in range(1, 6)]
    highs = [int(s.get("o", {}).get("hs", 0)) for s in stats]
    return f"Highest score in {fmt.upper()}: {max(highs)}"

def get_lowest_score(data, fmt="odi"):
    stats = [data.get(fmt, {}).get("sts", {}).get(str(i), {}) for i in range(1, 6)]
    lows = [int(s.get("o", {}).get("ls", 9999)) for s in stats]
    return f"Lowest ODI score: {min(lows)}"

def get_pace_performance(data):
    return f"Pace bowling conditions: {data.get('pit', {}).get('pbcd', 'N/A')}"

def get_last_match_winner(data, fmt="odi"):
    all_matches = data.get(fmt, {}).get("mch", {})
    if not all_matches:
        return "No matches found."
    latest = max(all_matches.items(), key=lambda x: x[1]['sdt'])[1]
    return f"Last match winner UID: {latest['wtuid']} in {latest['tle']}"