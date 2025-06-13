import streamlit as st
import pandas as pd
import os

# Título
st.title("Herramienta de Evaluación")

st.markdown("**Escala de respuesta:**")
st.markdown("1 = Totalmente en desacuerdo &nbsp;&nbsp; 2 = Parcialmente en desacuerdo &nbsp;&nbsp; 3 = Indiferente &nbsp;&nbsp; 4 = Parcialmente de acuerdo &nbsp;&nbsp; 5 = Totalmente de acuerdo", unsafe_allow_html=True)

# Nombre del participante
nombre = st.text_input("Nombre completo:")

# Definición de las preguntas
preguntas = {
    "Trabajo en equipo": [
        "Cuando trabajo en equipo, me esfuerzo por escuchar y respetar las ideas de mis compañeros.",
        "Participo activamente en las actividades grupales y cumplo con mis responsabilidades.",
        "Puedo comunicar claramente mis ideas hacia mis compañeros de equipo."
