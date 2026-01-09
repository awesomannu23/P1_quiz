import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

#This line finds your .env file and opens the secret box
load_dotenv("p1_quiz.env")
#This line gets the key safely
api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
# --- Simple Quiz UI ---
st.title("AI Quiz Generator 🤖")
st.subheader("Generate a quiz on any topic!")

topic = st.text_input("Enter a topic (e.g., Python Basics, Space, History):")
num_questions = st.slider("Number of questions", 1, 5, 3)

if st.button("Generate Quiz"):
    if topic:
        model = genai.GenerativeModel('gemini-3-flash-preview')
        prompt = f"Create a {num_questions} question multiple choice quiz about {topic}. Provide the answers at the end."
        with st.spinner("Generating..."):
                response = model.generate_content(prompt)
                st.write(response.text)
    else:
        st.warning("Please enter a topic first!")