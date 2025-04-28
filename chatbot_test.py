import streamlit as st
import google.generativeai as genai

# Configura tu API KEY (reemplaza AQUÍ_TU_API_KEY)
API_KEY = "AIzaSyBvzvYhvR3Eo2pyMIJKrrpZJGSGt2Lhw5U"
genai.configure(api_key=API_KEY)

# Crear modelo Gemini
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Título de la página
st.title("Chatbot de Mauricio Coloma 🚀")

# Entrada del usuario
user_input = st.text_input("Hazme una pregunta:")

# Cuando el usuario escribe algo
if user_input:
    try:
        response = model.generate_content(user_input)
        st.write("💬 Respuesta de Gemini:")
        st.write(response.text.strip())
    except Exception as e:
        st.error(f"[Error]: {e}")