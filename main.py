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

# Diccionario de respuestas
respuestas = {"Nombre": nombre}

# Mostrar preguntas
for categoria, items in preguntas.items():
    st.subheader(categoria)
    for pregunta in items:
        respuesta = st.radio(pregunta, [1, 2, 3, 4, 5], key=pregunta)
        respuestas[pregunta] = respuesta

# Guardar respuestas
if st.button("Enviar respuestas"):
    if nombre.strip() == "":
        st.warning("Por favor, escribe tu nombre.")
    else:
        archivo = "respuestas_evaluacion.csv"
        nueva_respuesta = pd.DataFrame([respuestas])
        if os.path.exists(archivo):
            datos_existentes = pd.read_csv(archivo)
            datos_combinados = pd.concat([datos_existentes, nueva_respuesta], ignore_index=True)
        else:
            datos_combinados = nueva_respuesta
        datos_combinados.to_csv(archivo, index=False)
        st.success("¡Respuestas guardadas exitosamente!")

# Descargar resultados
if os.path.exists("respuestas_evaluacion.csv"):
    with open("respuestas_evaluacion.csv", "rb") as f:
        st.download_button(
            label="Descargar respuestas en CSV",
            data=f,
            file_name="respuestas_evaluacion.csv",
            mime="text/csv"
        )
