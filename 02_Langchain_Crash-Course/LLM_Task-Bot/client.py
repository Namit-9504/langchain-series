import requests
import streamlit as st


def get_llma2_responce(input_text):
    """Fetches response from LLAMA2 API and handles potential decode errors.

    Args:
        input_text (str): The topic for the poem.

    Returns:
        str (or None): The generated poem or None if there's an error.
    """
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={'input': {'topic': input_text}},
        )
        response.raise_for_status()  # Raise an exception for unsuccessful status codes
        return response.json()['output']
    except requests.exceptions.RequestException as e:
        print(f"Error getting LLAMA2 response: {e}")
        st.error("An error occurred while processing the poem request.")
        return None


def get_gemma_responce(input_text):
    """Fetches response from Gemma API and handles potential decode errors.

    Args:
        input_text (str): The topic for the essay.

    Returns:
        str (or None): The generated essay or None if there's an error.
    """
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={'input': {'topic': input_text}},
        )
        response.raise_for_status()  # Raise an exception for unsuccessful status codes
        return response.json()['output']
    except requests.exceptions.RequestException as e:
        print(f"Error getting Gemma response: {e}")
        st.error("An error occurred while processing the essay request.")
        return None


st.title("Langchain Demo with LLAMA2 API & Gemma API")
input_text = st.text_input("write an essay on")
input_text1 = st.text_input("write a poem on")

if input_text:
    essay = get_gemma_responce(input_text)
    if essay:
        st.write(essay)

if input_text1:
    poem = get_llma2_responce(input_text1)
    if poem:
        st.write(poem)

