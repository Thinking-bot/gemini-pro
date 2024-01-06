import streamlit as st
import google.generativeai as genai
import os



API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("Gemini Pro")

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    return role


for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    st.chat_message('user').markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
