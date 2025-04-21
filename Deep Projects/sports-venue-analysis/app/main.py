import streamlit as st
from query_handler import answer_user_query

# Streamlit front-end for interaction
def streamlit_app():
    # Title of the app
    st.title("Venue Data Query System")

    # Input for venue name
    venue_name = st.text_input("Enter Venue Name:", "")
    
    # Input for the query
    user_query = st.text_area("Enter your query:")

    # Button to submit the query
    if st.button("Submit Query"):
        if venue_name and user_query:
            # Call function to process the query
            response = answer_user_query(user_query, venue_name)
            st.write(f"Answer: {response}")
        else:
            st.write("Please provide both venue name and query.")

# Run the Streamlit app
if __name__ == '__main__':
    streamlit_app()
