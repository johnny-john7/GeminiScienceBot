import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import pyttsx3



load_dotenv()

st.set_page_config(
    page_title="Mrs. Fox 🦊",
    page_icon=":fox:",  
    layout="centered",  
)

GOOGLE_API_KEY = os.getenv("YOUR GOOGLE_API_KEY")

gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

engine = None




def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


st.title("🪐Curious Cosmos: Your AI Guide to the Universe's Equations")


TOPIC_KEYWORDS = {
    "physics": ["mechanics", "electricity", "magnetism", "optics", "thermodynamics",
                 "quantum", "relativity", "nuclear physics", "particle physics",
                 "astrophysics", "cosmology"],
    "math": ["algebra", "calculus", "geometry", "statistics", "probability",
             "linear algebra", "differential equations", "discrete mathematics",
             "trigonometry", "number theory", "combinatorics", "logic"],
    "chemistry": ["atomic structure", "periodic table", "chemical bonding", "chemical reactions",
                 "acids and bases", "thermochemistry", "kinetics", "equilibrium",
                 "electrochemistry", "organic chemistry", "analytical chemistry",
                 "biochemistry", "inorganic chemistry"],
}

GREETING_KEYWORDS = ["hello", "hi", "hey", "how are you"]


user_prompt = st.chat_input("Ask here", key="user_prompt")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    if any(keyword in user_prompt.lower() for keyword in GREETING_KEYWORDS):
        greeting_response = "Hi there! How can I help you today?"
        st.chat_message("assistant").markdown(greeting_response)
    elif any(keyword in gemini_response.text.lower() for keyword in TOPIC_KEYWORDS.get("physics", [])):
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
    elif any(keyword in gemini_response.text.lower() for keyword in TOPIC_KEYWORDS.get("math", [])):
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
    elif any(keyword in gemini_response.text.lower() for keyword in TOPIC_KEYWORDS.get("chemistry", [])):
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
    else:
        info_message = (
            "While I'm still under development, I'm happy to help with various physics "
            "topics, including mechanics, electricity, and more (see the full list "
            "when asking about physics). I'm also expanding my knowledge in chemistry "
            "and math, where I can assist you with concepts like algebra, calculus, "
            "atomic structure, and chemical reactions. If you'd like to greet me, you "
            "can say things like 'hello' or 'hi'."
        )
        st.info(info_message)
