import streamlit as st
import google.generativeai as genai

# Aplicar estilo para que el texto de entrada se vea negro en móviles
st.markdown(
    """
    <style>
    input {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Configurar la API Key de Gemini usando el secrets.toml
genai.configure(api_key=st.secrets["api_key"])

# Crear el modelo
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Configuración de la página
st.set_page_config(page_title="Chatbot de Mauricio Coloma", page_icon="🤖", layout="centered")

# Título
st.markdown("<h1 style='text-align: center; color: green;'>🤖 Chatbot de Mauricio Coloma 🚀</h1>", unsafe_allow_html=True)

# Descripción
st.markdown('<h3 style="color: red;">Hazme una pregunta:</h3>', unsafe_allow_html=True)

# Área de texto para la pregunta
user_input = st.text_input("Hazme una pregunta:")

# Botones
col1, col2 = st.columns(2)

with col1:
    if st.button("Enviar"):
        if user_input:
            try:
                response = model.generate_content(user_input)
                st.success(response.text)
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
        else:
            st.warning("Por favor, escribe una pregunta antes de enviar.")

with col2:
    if st.button("Borrar"):
        st.experimental_rerun()