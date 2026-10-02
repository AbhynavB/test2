import os
import streamlit as st
from openai import OpenAI

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

key = os.environ.get("GEMINI_API_KEY")
if not key:
    st.error("GEMINI_API_KEY is not set. Ask your teacher for help.")
    st.stop()

client = OpenAI(api_key=key, base_url=BASE_URL)

st.title("Hello, AI")
prompt = st.text_input("Ask me anything")
if prompt:
    reply = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    st.write(reply.choices[0].message.content)

st.divider()
st.caption("Environment checks (remove before class)")
st.file_uploader("Test file upload", type=["pdf", "txt"])
st.audio_input("Test microphone")
