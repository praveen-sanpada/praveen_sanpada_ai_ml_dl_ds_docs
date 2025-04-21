import streamlit as st
import openai


st.title("📝 Simple Text Generator")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # You can change to gpt-4 if you have access
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )
            text_output = response['choices'][0]['message']['content']
            st.subheader("Generated Text:")
            st.write(text_output)
