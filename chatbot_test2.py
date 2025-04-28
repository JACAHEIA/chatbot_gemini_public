import streamlit as st
import google.generativeai as genai

# Configurar tu API KEY de Gemini (ponla aquí directamente o usa st.secrets si prefieres ocultarla)
genai.configure(api_key="AIzaSyBvzvYhvR3Eo2pyMIJKrrpZJGSGt2Lhw5U")

# ---- Diseño: Fondo, título y descripción ----
page_bg_img = '''
<style>
.stApp {
background-color: #f5f5f5;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🤖 Chatbot de Mauricio Coloma 🚀</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Este chatbot responde tus preguntas usando IA avanzada de Gemini. ¡Escribe cualquier duda!</p>",
    unsafe_allow_html=True
)

# ---- Entrada del usuario ----
user_input = st.text_input("Hazme una pregunta:")

# ---- Botón para enviar la pregunta ----
if st.button("Enviar"):
    if user_input:
        try:
            model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
            response = model.generate_content(user_input)
            st.subheader("💬 Respuesta de Gemini:")
            st.write(response.text.strip())
        except Exception as e:
            st.error(f"[Error] Algo salió mal: {e}")
    else:
        st.warning("⚠️ Por favor escribe una pregunta antes de enviar.")

# ---- Botón para borrar todo ----
if st.button("Borrar"):
    st.experimental_rerun()

# ---- Pie de página ----
st.markdown(
    "<footer style='text-align: center; margin-top: 50px; color: #888;'>Creado por Mauricio Coloma 💻</footer>",
    unsafe_allow_html=True
)