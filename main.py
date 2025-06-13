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
            st.subheader("Respuestas registradas:")
            st.dataframe(df)

            with open(archivo, "rb") as f:
                st.download_button(
                    label="📥 Descargar respuestas en CSV",
                    data=f,
                    file_name="respuestas_evaluacion.csv",
                    mime="text/csv"
                )
        else:
            st.info("Aún no hay respuestas registradas.")

    elif username or password:
        st.error("Credenciales incorrectas.")

elif rol == "Estudiante":
    st.subheader("Formulario de evaluación")
    nombre = st.text_input("Escribe tu nombre completo:")

    if nombre.strip():
        st.markdown("**Escala de respuesta:**")
        st.markdown("1 = Totalmente en desacuerdo &nbsp;&nbsp; 2 = Parcialmente en desacuerdo &nbsp;&nbsp; 3 = Indiferente &nbsp;&nbsp; 4 = Parcialmente de acuerdo &nbsp;&nbsp; 5 = Totalmente de acuerdo", unsafe_allow_html=True)

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
        for categoria, items in preguntas.items():
            st.subheader(categoria)
            for pregunta in items:
                respuesta = st.radio(pregunta, [1, 2, 3, 4, 5], key=pregunta)
                respuestas[pregunta] = respuesta

        if st.button("Enviar respuestas"):
            archivo = "respuestas_evaluacion.csv"
            nueva_respuesta = pd.DataFrame([respuestas])
            if os.path.exists(archivo):
                datos_existentes = pd.read_csv(archivo)
                datos_combinados = pd.concat([datos_existentes, nueva_respuesta], ignore_index=True)
            else:
                datos_combinados = nueva_respuesta
            datos_combinados.to_csv(archivo, index=False)
            st.success("¡Respuestas enviadas exitosamente!")
    else:
        st.info("Por favor, ingresa tu nombre para comenzar.")
