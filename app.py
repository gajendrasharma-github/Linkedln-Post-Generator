import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()
    
# Fetch the API Key
api_key = st.secrets.get('API_KEY') or os.getenv('API_KEY')

genai.configure(api_key=api_key)

# Model
model = genai.GenerativeModel(model_name="gemini-2.0-flash-lite")

# Sidebar Inputs
st.sidebar.title("Customize Your LinkedIn Post")

word_count_range = st.sidebar.selectbox(
    "Select Word Count Range", 
    ["50-100", "100-250", "250-500", "500-800"]
)
tone_choice = st.sidebar.selectbox("Tone", ["Friendly", "Professional", "Inspirational", "Informative", "Casual", "Conversational", "Thought-Provoking", "Storytelling", "Humorous", "Expert"])
audience_choice = st.sidebar.selectbox("Audience", ["Professionals", "Students", "Entrepreneurs"])
goal = st.sidebar.text_input("Goal (e.g., Build Brand, Establish Expertise)")
structure_choice = st.sidebar.selectbox("Structure", ["Bullets", "Small Paragraphs", "One Long Paragraph"])
opening_choice = st.sidebar.selectbox("Opening Line Type", ["Question", "Surprising Fact", "Statistic", "Bold Statement"])
emoji_choice = st.sidebar.radio("Include Emojis?", ("Yes", "No"))
real_life_example = st.sidebar.radio("Real-Life Example?", ("Yes", "No"))
cta = st.sidebar.radio("Include Call-to-Action?", ("Yes", "No"))
hashtags = st.sidebar.radio("Include Hashtags?", ("Yes", "No"))

# Final prompt construction
word_count_map = {
    "50-100": "Write a post between 50 to 100 words.",
    "100-250": "Write a post between 100 to 250 words.",
    "250-500": "Write a post between 250 to 500 words.",
    "500-800": "Write a post between 500 to 800 words."
}

# Main Inputs
st.title("🚀 LinkedIn Post Generator")
topic = st.text_input("Enter Topic")

if st.button("Generate LinkedIn Post"):
    final_prompt = (
        f"Write a {tone_choice} LinkedIn post about '{topic}', targeting {audience_choice}. "
        f"Goal: {goal}. Structure: {structure_choice}. Opening: {opening_choice}. "
        f"Use simple, everyday language without jargon. Keep vocabulary easy to understand. "
        f"Sound human, natural, and relatable. Write with warmth and emotional connection. "
        f"Emojis: {emoji_choice}. Include real-life example: {real_life_example}. "
        f"Include CTA: {cta}. Include hashtags: {hashtags}."
        f"{word_count_map[word_count_range]}."
    )

    response = model.generate_content(final_prompt)
    st.subheader("Generated LinkedIn Post:")
    st.write(response.text)