import streamlit as st
from chatbot import ask_gemini_ai
import webbrowser  # for opening emergency links
from googletrans import Translator

st.set_page_config(page_title="🚗 VEHICARE", layout="wide")
st.title("🚗 VEHICARE")

translator = Translator()

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "language" not in st.session_state:
    st.session_state.language = "English"

# Sidebar Settings
with st.sidebar:
    st.markdown("## ⚙ Settings")

    # Language selection
    language = st.selectbox(
        "Language 🌐",
        ["English", "Hindi", "Telugu"],
        index=["English", "Hindi", "Telugu"].index(st.session_state.language)
    )
    st.session_state.language = language

    # Rating
    st.markdown("## ⭐ Rate This Chatbot")
    rating = st.slider("How would you rate your experience?", 1, 5, 3)
    if st.button("Submit Rating"):
        st.success(f"Thanks for your {rating} star rating!")

    # Partner link
    st.markdown("---")
    st.markdown("### Partner Services")
    st.markdown("[GoMechanic](https://gomechanic.in) 🔗")

    # Emergency button
    st.markdown("## 🚨 Emergency Help")
    if st.button("Call Roadside Assistance"):
        st.warning("Dialing roadside assistance: 1800-112-112 📞")
        # You could also open a link if available:
        # webbrowser.open("tel:1800112112")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Ask me about your vehicle issues...")

if user_input:
    st.chat_message("user").write(user_input)

    with st.spinner("Thinking...🤔"):
        bot_response = ask_gemini_ai(user_input, st.session_state.chat_history)

    # Translate response if needed
    if st.session_state.language != "English":
        translated = translator.translate(bot_response, dest=st.session_state.language.lower()[0:2])
        bot_response = translated.text

    st.chat_message("assistant").write(bot_response)

    # Save chat
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": bot_response})