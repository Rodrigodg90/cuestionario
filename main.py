import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(page_title="Evaluación de habilidades", layout="centered")

st.title("HERRAMIENTA DE EVALUACIÓN")

st.markdown("**Escala Likert:**  
1 = Totalmente en desacuerdo  
2 = Parcialmente en desacuerdo  
3 = Indiferente  
4 = Parcialmente de acuerdo  
5 = Totalmente de acuerdo")

# Identificador del estudiante
nombre = st.text_input("Por favor, ingresa tu nombre o matrícula:")

if nombre:
    # Definición de preguntas
    preguntas = {
        "Trabajo en equipo": [
            "Cuando trabajo en equipo, me esfuerzo por escuchar y respetar las ideas de mis compañeros.",
            "Participo activamente en las actividades grupales y cumplo con mis responsabilidades.",
            "Puedo comunicar claramente mis ideas hacia mis compañeros de equipo.",
            "Suelto intervenir de manera asertiva en los conflictos dentro del equipo para resolverlos."
        ],
        "Trabajo autónomo en casa": [
            "Completo las tareas escolares en tiempo y forma.",
            "Busco recursos o soluciones por mi cuenta para resolver las dudas que tengo antes de pedir ayuda.",
            "Estudio material de clase constantemente."
        ],
        "Comprensión lectora": [
            "Puedo identificar las ideas principales y los detalles importantes en los textos que leo.",
            "Comprendo instrucciones escritas sin necesidad de explicaciones adicionales.",
            "Después de leer un texto, puedo resumirlo con mis propias palabras de forma clara."
        ]
    }

    respuestas = {"Nombre": nombre}

    with st.form("formulario_evaluacion"):
        for categoria, items in preguntas.items():
            st.subheader(categoria)
            for pregunta in items:
                respuestas[pregunta] = st.radio(
                    label=pregunta,
                    options=[1, 2, 3, 4, 5],
                    key=pregunta,
                    horizontal=True
                )
        submit = st.form_submit_button("Enviar respuestas")

    if submit:
        # Cargar archivo existente o crear nuevo
        try:
            df = pd.read_csv("respuestas.csv")
        except FileNotFoundError:
            df = pd.DataFrame()

        # Agregar nueva fila
        nueva_fila = pd.DataFrame([respuestas])
        df = pd.concat([df, nueva_fila], ignore_index=True)
        df.to_csv("respuestas.csv", index=False)
        st.success("¡Respuestas registradas correctamente!")

        # Mostrar tabla actual
        st.subheader("Respuestas acumuladas:")
        st.dataframe(df)

        # Descargar CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Descargar todas las respuestas en CSV", csv, "respuestas.csv", "text/csv")

