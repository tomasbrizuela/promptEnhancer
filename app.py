# -*- coding: utf-8 -*-
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_gemini_content(prompt):
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text

st.title("Ingresá tu idea 💡")
st.subheader("Crearemos el mejor prompt para vos")

# Inicializar el estado de la variable
if "gemini_response" not in st.session_state:
    st.session_state.gemini_response = ""

userInput = st.text_input("Que querés saber?")

prompt = f"Tu objetivo es tomar este texto que ingresa el usuario: {userInput}. Entendé lo que quiere el usuario y potencia, optimizá y devolvé SOLAMENTE un prompt que yo pueda directamente copiar y pegar en una IA para obtener el mejor resultado posible. Devolvé solo el prompt optimizado, sin texto adicional ni comillas"

if st.button("Enviar"):
    st.session_state.gemini_response = generate_gemini_content(prompt)

if st.session_state.gemini_response:
    st.subheader("El mejor prompt para tu objetivo es: ")
    st.write(st.session_state.gemini_response)

    if st.button("Probar Prompt 🚀"):
        gemini_response2 = generate_gemini_content(st.session_state.gemini_response.split())
        st.write(gemini_response2)

st.header("Cómo funciona? 🤓")
st.write("Esta aplicación web te ayuda a generar prompts optimizados para modelos de IA. Simplemente ingresa tu idea o pregunta en el cuadro de texto, y la app utilizará un modelo de lenguaje avanzado para crear un prompt refinado que te permitirá obtener los mejores resultados de otros modelos de IA. Una vez generado el prompt optimizado, puedes hacer clic en el botón 'Probar Prompt 🚀' para probarlo y ver la respuesta de la IA.")
