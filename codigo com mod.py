import streamlit as st
import google.generativeai as genai

# Configura a chave a partir dos secrets
genai.configure(api_key=st.secrets["AQ.Ab8RN6JVoAsSqdiWq_anx7yRa_MHZ84DqXgIM9HixwdHWID3Bg"])

modelo = genai.GenerativeModel("gemini-flash-lite-latest")

st.write("## Yellow AI (Alpha)")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})

    resposta = modelo.generate_content(st.session_state["lista_mensagens"])
    resposta_ia = resposta.text

    st.chat_message("assistant").write(resposta_ia)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})