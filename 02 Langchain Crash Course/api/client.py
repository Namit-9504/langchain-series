import requests
import streamlit as st

def get_gemma_responce(input_text):
    response=requests.post(
    "http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

def get_llma2_responce(input_text):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

st.title("Langchain Demo with LLAMA2 API & Gemma API")
input_text=st.text_input("write an essay on")
input_text1=st.text_input("wite a poem on")

if input_text:
    st.write(get_llma2_responce(input_text))

if input_text1:
    st.write(get_llma2_responce(input_text1))