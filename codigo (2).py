import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(
    api_key=st.secrets["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

st.write("## Yellow AI (Alpha)")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["lista_mensagens"].append(
        {"role": "user", "content": mensagem_usuario}
    )

    resposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest",
    )

    resposta_ia = resposta_modelo.choices[0].message.content
    st.chat_message("assistant").write(resposta_ia)
    st.session_state["lista_mensagens"].append(
        {"role": "assistant", "content": resposta_ia}
    )