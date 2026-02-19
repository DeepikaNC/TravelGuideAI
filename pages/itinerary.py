import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Your Itinerary", page_icon="✈️")

st.title("📍 Your Personalized Itinerary")

# Retrieve data from session state
destination = st.session_state.get("destination")
days = st.session_state.get("days")
nights = st.session_state.get("nights")
interests = st.session_state.get("interests")

if destination and days and nights:

    with st.spinner("Generating your personalized itinerary..."):

        prompt = f"""
        Create a short and simple {days}-day travel itinerary for {destination}.

        User interests: {interests}

        Give:
        - Day-wise plan
        - 2–3 main attractions per day
        - 2 food recommendations per day
        - Short travel tips
        - Short cultural insights

        Keep response within 100-150 words.
        """

        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error generating itinerary: {e}")

else:
    st.warning("No travel details found. Please go back.")

# Back button
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")
