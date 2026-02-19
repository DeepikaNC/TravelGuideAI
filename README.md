# 🌍 TravelGuideAI
TravelGuideAI is an intelligent web application that creates personalized travel itineraries based on user preferences.
Users enter their destination, trip duration, and interests to receive a structured day-wise travel plan.
It simplifies trip planning by providing attractions, food suggestions, cultural insights, and travel tips in one place.

**🚀 Tech Stack**

Python 3.11
Streamlit
Google Generative AI 

**Project Structure**
travelguideai/
│
├── app.py
├── requirements.txt
└── pages/
      └── itinerary.py

**How to Run This Project Locally**
1️⃣ Clone the Repository
git clone https://github.com/your-username/travelguideai.git
cd travelguideai

2️⃣ Install Dependencies

Make sure Python 3.10+ is installed.

pip install -r requirements.txt

3️⃣ Add Your Gemini API Key

*On Windows (PowerShell):*
setx GEMINI_API_KEY "your_api_key_here"

*On Mac/Linux:*

export GEMINI_API_KEY="your_api_key_here"
Restart terminal after setting the key.

4️⃣ Run the App
streamlit run app.py

**Conclusion**
TravelGuideAI makes trip planning simple by generating personalized, structured itineraries based on user preferences.
It saves time and provides clear, customized travel suggestions in one convenient platform.
