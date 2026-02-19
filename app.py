import streamlit as st

st.set_page_config(page_title="TravelGuideAI", page_icon="🌍")

st.title("🌍 Travel Itinerary Generator")
st.write("Generate a personalized travel itinerary using AI")

destination = st.text_input("Enter your travel destination:")
days = st.number_input("Enter number of days:", min_value=1, step=1)
nights = st.number_input("Enter number of nights:", min_value=1, step=1)
interests = st.text_input("Enter your interests (e.g., adventure, food, spirituality):")

if st.button("Generate Itinerary"):

    if destination and days and nights:

        # Store data in session state
        st.session_state.destination = destination
        st.session_state.days = days
        st.session_state.nights = nights
        st.session_state.interests = interests

        # Switch to next page
        st.switch_page("pages/itinerary.py")

    else:
        st.warning("Please fill all required fields.")


