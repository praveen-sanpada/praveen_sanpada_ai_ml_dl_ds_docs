import streamlit as st
import openai
import requests

# SET THESE KEYS
OPENAI_API_KEY = "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"
CRICKET_API_KEY = "6cef0716-4c8b-4033-9354-f16a61d01a33"

# Set your OpenAI key
openai.api_key = OPENAI_API_KEY

# Function to get recent IPL matches
def get_recent_matches():
    url = "https://api.cricapi.com/v1/currentMatches?apikey=" + CRICKET_API_KEY
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data', [])
    return []

# Function to find latest T20 IPL match at a specific venue
def find_latest_match(matches, venue_keyword):
    for match in matches:
        if ("ipl" in match.get('name', '').lower()
                and "t20" in match.get('matchType', '').lower()
                and venue_keyword.lower() in match.get('venue', '').lower()):
            return match
    return None

# Streamlit UI
st.title("🏏 Cricket Smart Answer Bot")

user_question = st.text_input("Ask your cricket question (e.g. Last T20 IPL match at Chennai):")

if st.button("Get Answer"):
    with st.spinner("Thinking..."):
        matches = get_recent_matches()

        # Use OpenAI to parse the venue from the user question
        prompt = f"""Extract the venue from this cricket question:
        "{user_question}"
        Respond with just the venue name like 'Chennai' or 'Mumbai'."""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10
        )
        venue = response['choices'][0]['message']['content'].strip()

        match = find_latest_match(matches, venue)
        if match:
            st.subheader("Match Found:")
            st.write(f"🏟️ Venue: {match.get('venue')}")
            st.write(f"🆚 {match.get('teams')[0]} vs {match.get('teams')[1]}")
            st.write(f"📅 Date: {match.get('date')}")
            st.write(f"📊 Status: {match.get('status')}")
            st.write(f"🏏 Score: {match.get('score')}")
        else:
            st.error("No matching IPL T20 match found for that venue.")
