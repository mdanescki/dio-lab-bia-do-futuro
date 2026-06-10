import streamlit as st
from agente import conversar

st.set_page_config(
    page_title="Orça - Assistente Financeiro",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Orça")
st.caption("Seu assistente financeiro pessoal")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            resposta = conversar(prompt)
        st.write(resposta)

    st.session_state.mensagens.append({"role": "assistant", "content": resposta})