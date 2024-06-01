import os

import google.generativeai as genai
import PIL.Image
import streamlit as st

# Fetching the API_KEY from the system's environmental variable
API_KEY = os.environ["GOOGLE_GEMINI_API"]

# Configuring the genai api_key
genai.configure(api_key=API_KEY)

# Loading and a function to get response from the gemini model
model = genai.GenerativeModel("gemini-pro-vision")


def get_response(image, text=""):
    if text != "":
        response = model.generate_content([text, image])
        return response.text
    response = model.generate_content(image)
    return response.text


# Front-end for the Gemini LLM App
st.header("Gemini LLM multimodal imput's")

input_prompt = st.text_input("Enter a prompt here")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
image = ""
if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Submit")

# Write the response if the submit button is clicked
if submit:
    response = get_response(image, input_prompt)
    st.subheader("The Respose is : ")
    st.write(response)
