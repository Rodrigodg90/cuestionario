import streamlit as st
import pandas as pd
import os

# --- CONFIGURACIÓN ---
ADMIN_USERNAME = "profesor"
ADMIN_PASSWORD = "1234"  # Puedes cambiarla a algo más seguro

# --- LOGIN SIMPLE ---
st.title("Ingreso a la Herramienta de Evaluación")

rol = st.radio("Selecciona tu rol:", ["Estudiante", "Profesor"])

if rol == "Profesor":
    username = st.text_input("Usuario:")
    password = st.text_input("Contraseña:", type="password")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        st.success("Acceso concedido como profesor.")
        
        # Mostrar resultados si existen
        archivo = "respuestas_evaluacion.csv"
        if os.path.exists(archivo):
            df = pd.read_csv(archivo)
            st.subhe
