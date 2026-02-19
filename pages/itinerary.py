import streamlit as st
import google.generativeai as genai
import os

# Configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("📍 Your Personalized Itinerary")

# Get stored data
destination = st.session_state.get("destination")
days = st.session_state.get("days")

if destination and days:

    prompt = f"""
    Create a short {days}-day itinerary for {destination}.
    User interests: {interests}

                    Give:
                        - Day-wise plan
                        - 2–3 main attractions per day
                        - 2 food recommendation per day
                        - Travel tips in short
                        - Cultural insights in short

    Keep the response concise and within 150–180 words.
   
    """

    try:
        response = model.generate_content(prompt)
        st.write(response.text)

    except Exception:
        st.error("Error generating itinerary.")

else:
    st.warning("No trip details found. Please go back.")
