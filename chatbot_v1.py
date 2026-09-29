# chatbot.py
import google.generativeai as genai
import json
from config import GEMINI_API_KEY, SYSTEM_PROMPT

# Load service center data at startup
with open("service_centers.json", "r") as file:
    SERVICE_CENTERS = json.load(file)

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

def get_service_center_info(location):
    """Fetch service center details if available in JSON."""
    center = SERVICE_CENTERS.get(location)
    if center:
        return (
            f"🚗 *Service Center in {location}*\n"
            f"- *Rating:* {center['rating']} ⭐\n"
            f"- *Phone:* {center['phone']}\n"
            f"- *Timings:* {center['timings']}\n"
            f"- *Address:* {center['address']}"
        )
    return None

def ask_gemini_ai(user_message):
    """Query Gemini AI with an optimized system prompt."""
    
    # Check if the user is asking about service centers
    words = user_message.lower().split()
    for location in SERVICE_CENTERS.keys():
        if location.lower() in words:
            center_info = get_service_center_info(location)
            if center_info:
                return center_info

    # Call Gemini AI only if service center info is not found
    model = genai.GenerativeModel("gemini-3.6-flash")  # Choose the appropriate model
    response = model.generate_content(f"{SYSTEM_PROMPT}\nUser: {user_message}\nAI:")

    return response.text.strip() if response else "I'm sorry, I couldn't process that request."