import os

import google.generativeai as genai
import streamlit as st

# Fetching the Gemini API key from the system environmental variables
API_KEY = os.environ["GOOGLE_GEMINI_API"]

# Configuring the api_key
genai.configure(api_key=API_KEY)

# functions for loading and getting response from the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")


def get_response(input_prompt):
    response = model.generate_content(input_prompt)
    return response.text


# Creating a Front-end for the Gemini-LLM application
st.header("Gemini LLM App")
input_prompt = st.text_input("What do you need to ask ?")
button = st.button("Submit")

if button:
    st.subheader("The Response is : ")
    st.write(get_response(input_prompt))
