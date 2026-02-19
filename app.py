import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API using environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="TravelGuideAI", page_icon="🌍")

st.title("🌍 Travel Itinerary Generator")
st.write("Generate a personalized travel itinerary using AI")

destination = st.text_input("Enter your travel destination:")
days = st.number_input("Enter number of days:", min_value=1, step=1)
nights = st.number_input("Enter number of nights:", min_value=1, step=1)
interests = st.text_input("Enter your interests (e.g., adventure, food, spirituality):")

if st.button("Generate Itinerary"):

    if destination and days and nights:

        with st.spinner("Generating your personalized itinerary..."):

            prompt = f"""
                Create a short and simple {days}-day travel itinerary for {destination}.

                    User interests: {interests}

                    Give:
                        - Day-wise plan
                        - 2–3 main attractions per day
                        - 2 food recommendation per day
                        - Travel tips in short
                        - Cultural insights in short

                    Keep the response concise and within 150–200 words.
            """


            response = model.generate_content(prompt)

            st.subheader("📍 Your Personalized Itinerary:")
            st.markdown(response.text)

    else:
        st.warning("Please fill all required fields.")
