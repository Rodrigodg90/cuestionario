import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Examen Unidad 1", layout="centered")

st.title("Examen Unidad 1 – Fundamentos de Programación Orientada a Objetos")
st.write("**Profesor:** Dr. Rodrigo Delgadillo Gaytán")

# Verificación de sesión para envío único
if 'enviado' not in st.session_state:
    st.session_state['enviado'] = False

# Nombre del alumno
nombre = st.text_input("Ingresa tu nombre completo para comenzar el examen:")

if nombre:
    st.success("¡Bienvenido/a, {}! A continuación, responde el examen:".format(nombre))

    # Preguntas de opción múltiple
    preguntas = [
        {
            "texto": "1. ¿A qué concepto nos referimos cuando hablamos de un modelo o estilo de programación que guía la forma en que se estructura y organiza el código?",
            "opciones": ["Sintaxis", "Compilador", "Paradigma de programación", "Entorno de desarrollo"]
        },
        {
            "texto": "2. ¿Cuál de las siguientes opciones describe mejor la programación imperativa?",
            "opciones": [
                "Un estilo que se enfoca en lo que debe hacerse, no en cómo",
                "Un enfoque donde se describe paso a paso cómo debe ejecutarse una tarea",
                "Un modelo basado en lógica matemática",
                "Un paradigma centrado en la interfaz gráfica del usuario"
            ]
        },
        {
            "texto": "3. ¿Cuál de los siguientes NO es un paradigma de programación?",
            "opciones": ["Imperativa", "Funcional", "Compilada", "Orientada a objetos"]
        },
        {
            "texto": "4. ¿Qué es la programación visual?",
            "opciones": [
                "Programación visual",
                "Programación funcional",
                "Programación declarativa",
                "Programación estructurada"
            ]
        },
        {
            "texto": "5. ¿Cuál de las siguientes opciones corresponde al paradigma que organiza el código en clases y objetos?",
            "opciones": [
                "Programación estructurada",
                "Programación funcional",
                "Programación orientada a objetos",
                "Programación visual"
            ]
        },
        {
            "texto": "6. ¿Qué es un entorno visual de desarrollo?",
            "opciones": [
                "Un lenguaje de programación para interfaces",
                "Una forma de programar sin código",
                "Una herramienta para diseñar y programar visualmente",
                "Un sistema operativo especializado para programación"
            ]
        },
        {
            "texto": "7. ¿Cuáles son los cuatro pilares de la programación orientada a objetos?",
            "opciones": [
                "Funciones, métodos, atributos, operadores",
                "Herencia, encapsulamiento, polimorfismo, abstracción",
                "Visualización, compilación, modelado, ejecución",
                "Clases, objetos, métodos, estructuras"
            ]
        },
        {
            "texto": "8. ¿Qué es la herencia?",
            "opciones": ["Encapsulamiento", "Abstracción", "Herencia", "Polimorfismo"]
        },
        {
            "texto": "9. ¿Qué opción describe mejor el polimorfismo?",
            "opciones": [
                "El proceso de ocultar datos",
                "La capacidad de una clase para definirse dentro de otra",
                "Capacidad de un objeto para tener diferentes comportamientos con el mismo método",
                "La reutilización de código mediante ciclos"
            ]
        }
    ]

    respuestas = []
    for idx, pregunta in enumerate(preguntas):
        respuesta = st.radio(pregunta["texto"], pregunta["opciones"], key=f"pregunta_{idx}")
        respuestas.append(respuesta)

    # Preguntas abiertas
    st.markdown("### 10. Conceptos y ejemplos")
    st.info("Define con tus propias palabras y da un ejemplo de: Clase, Objeto, Atributo y Método.\n\nEscríbelo en una hoja libre y entrégalo al final.")
    pregunta_10_ok = st.checkbox("He completado la pregunta 10 en hoja libre.")

    st.markdown("### 11. Modelo conceptual con herencia")
    st.info("Diseña un modelo con una clase padre (3 atributos, 2 métodos) y dos clases hijas (cada una con 1 atributo y 1 método). Entrégalo en hoja libre.")
    pregunta_11_ok = st.checkbox("He completado la pregunta 11 en hoja libre.")

    # Botón de enviar
    if st.button("Terminar examen"):
        if st.session_state['enviado']:
            st.warning("Ya enviaste el examen en esta sesión.")
        else:
            # Guardar respuestas
            datos = {
                "Nombre": nombre,
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            for i, r in enumerate(respuestas, 1):
                datos[f"Pregunta_{i}"] = r
            datos["Pregunta_10_OK"] = "Sí" if pregunta_10_ok else "No"
            datos["Pregunta_11_OK"] = "Sí" if pregunta_11_ok else "No"

            # Guardar en archivo CSV
            df = pd.DataFrame([datos])
            try:
                df_ant = pd.read_csv("respuestas_examen.csv")
                df = pd.concat([df_ant, df], ignore_index=True)
            except FileNotFoundError:
                pass
            df.to_csv("respuestas_examen.csv", index=False)

            st.success("✅ ¡Examen enviado con éxito! Puedes entregar tus respuestas escritas.")
            st.session_state['enviado'] = True
else:
    st.warning("Por favor, escribe tu nombre completo para comenzar el examen.")
