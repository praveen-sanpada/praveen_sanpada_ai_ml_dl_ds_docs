import streamlit as st
from app.queries import handle_user_query

# Streamlit App Interface
def run_app():
    st.title("Cricket Venue Analytics")
    
    # Input section for user queries
    query = st.text_input("Ask a question about a cricket venue:")
    
    if query:
        response = handle_user_query(query)
        st.write(response)

if __name__ == "__main__":
    run_app()
