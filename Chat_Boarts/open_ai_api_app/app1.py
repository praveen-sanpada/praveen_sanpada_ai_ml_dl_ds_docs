import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual key

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
