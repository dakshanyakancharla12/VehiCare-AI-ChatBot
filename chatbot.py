import google.generativeai as genai
import json
from config import GEMINI_API_KEY, SYSTEM_PROMPT

# Load service center data at startup
with open("service_centers.json", "r") as file:
    SERVICE_CENTERS = json.load(file)

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

def get_service_center_info(location):
    """Fetch and format service center details from JSON."""
    center = SERVICE_CENTERS.get(location)
    if center:
        return (
            f"🚗 *Service Center in {location}*\n\n"
            f"⭐ *Rating:* {center['rating']}\n"
            f"📞 *Phone:* {center['phone']}\n"
            f"🕒 *Timings:* {center['timings']}\n"
            f"📍 *Address:* {center['address']}"
        )
    return None

# Load the videos JSON data (you can either load this from a file or hard-code it)
videos = {
    "Flat Tire Repair": {"The Youtube video": "https://www.youtube.com/embed/joBmbh0AGSQ"},
    "Battery Jumpstart": {"The Youtube video": "https://youtu.be/ZhVpxYlyLto?si=Eg0KZcTRxIYu3iI7"},
    "Engine Overheating": {"The Youtube video": "https://youtu.be/SVFflI-VTHg?si=UKj2-6Kb7xK-hb2V"},
    "Changing Oil": {"The Youtube video": "https://youtu.be/L4lc0meYkDY?si=oZETV0PIvcZRb4Ms"},
    "Brake Repair": {"The Youtube video": "https://youtu.be/21L9_ISeVAE?si=tUILjx-nJr_JdYuJ"},
    "Replacing Air Filter": {"The Youtube video": "https://youtu.be/RdXVxbd59es?si=GHIk14R6DMhyHR2l"},
    "Fixing a Dead Car Battery": {"The Youtube video": "https://youtu.be/lqd-A6bteqw?si=nTQjLrjzeJqvVlSB"},
    "Car Won't Start": {"The Youtube video": "https://youtu.be/fRfPupikHT4?si=XfqY8sEofix4iJk2"},
    "Flashing Check Engine Light": {"The Youtube video": "https://youtu.be/-wKmjxZKB4g?si=jzvtxr0aL-Coss0c"},
    "Replacing Spark Plugs": {"The Youtube video": "https://youtu.be/5iuSgGfwBBY?si=cQkffpY7op-FamBh"}
}

# Keywords to map vehicle issues to video names
problem_keywords = {
    "flat tire": "Flat Tire Repair",
    "dead battery": "Fixing a Dead Car Battery",
    "engine overheating": "Engine Overheating",
    "car won't start": "Car Won't Start",
    "oil change": "Changing Oil",
    "brake repair": "Brake Repair",
    "air filter": "Replacing Air Filter",
    "spark plugs": "Replacing Spark Plugs",
    "battery jumpstart": "Battery Jumpstart",
    "check engine light": "Flashing Check Engine Light"
}

def ask_gemini_ai(user_message, chat_history):
    """Query Gemini AI with chat history and optimized system prompt."""
    
    # Check for service center location first
    words = user_message.lower().split()
    for location in SERVICE_CENTERS.keys():
        if location.lower() in words:
            center_info = get_service_center_info(location)
            if center_info:
                return center_info

    # Prepare messages in the correct format for Gemini AI
    messages = [{"role": "assistant", "parts": [SYSTEM_PROMPT]}] + [
        {"role": msg["role"], "parts": [msg["content"]]} for msg in chat_history
    ] + [{"role": "user", "parts": [user_message]}]

    # Call Gemini AI
    model = genai.GenerativeModel("gemini-3.6-flash")  
    response = model.generate_content(messages)

    # Get AI response content
    ai_response = response.text.strip() if response else "I'm sorry, I couldn't process that request."
    
    # Check for matching vehicle issue in the user's message
    video_recommendation = None
    for keyword, issue in problem_keywords.items():
        if keyword in user_message.lower():
            video_recommendation = videos.get(issue, {}).get("The Youtube video")
            break
    
    # If a video recommendation is found, append the YouTube link to the AI response
    if video_recommendation:
        ai_response += f"\n\nYou can find more help in this video: {video_recommendation}"

    return ai_response