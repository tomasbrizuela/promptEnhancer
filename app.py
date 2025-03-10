# -*- coding: utf-8 -*-
import streamlit as st

st.title("Ingresá tu idea")
st.subheader("Crearemos el mejor prompt para vos")

prompt = st.text_input("Idea")

if st.button("Enviar"):
    st.write("Prompt enviado!")
