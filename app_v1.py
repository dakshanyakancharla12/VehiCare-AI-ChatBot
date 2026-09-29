import streamlit as st
import random
from datetime import datetime
import requests

# API Key
API_KEY = "1J2zyBBxsO2YWFxA7qzg6uZjkrLSi650"

# Configure page
st.set_page_config(page_title="Vehicare", page_icon="🚗", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 10px;
        padding: 20px;
    }
    .user-message {
        align-self: flex-end;
        background-color: #0078D4;
        color: white;
        border-radius: 15px 15px 0 15px;
        padding: 10px 15px;
        max-width: 70%;
    }
    .bot-message {
        align-self: flex-start;
        background-color: #F0F0F0;
        color: black;
        border-radius: 15px 15px 15px 0;
        padding: 10px 15px;
        max-width: 70%;
    }
    .header {
        text-align: center;
        margin-bottom: 20px;
    }
    .logo {
        width: 80px;
        height: 80px;
        margin: 0 auto;
    }
    .service-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    .sidebar-option {
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# Service stations data (Indian locations)
SERVICE_STATIONS = {
    "Tenali": {
        "rating": 4.5,
        "phone": "+91 9876543210",
        "timings": "9:00 AM - 8:00 PM",
        "address": "Main Road, Tenali, Andhra Pradesh"
    },
    "Mangalagiri": {
        "rating": 4.2,
        "phone": "+91 8765432109",
        "timings": "8:30 AM - 7:30 PM",
        "address": "NH16, Mangalagiri, Andhra Pradesh"
    },
    "Vijayawada": {
        "rating": 4.7,
        "phone": "+91 7654321098",
        "timings": "8:00 AM - 9:00 PM",
        "address": "Benz Circle, Vijayawada, Andhra Pradesh"
    },
    "Guntur": {
        "rating": 4.3,
        "phone": "+91 6543210987",
        "timings": "9:00 AM - 8:00 PM",
        "address": "Arundelpet, Guntur, Andhra Pradesh"
    },
    "Hyderabad": {
        "rating": 4.8,
        "phone": "+91 9432109876",
        "timings": "8:00 AM - 10:00 PM",
        "address": "Banjara Hills, Hyderabad, Telangana"
    },
    "Tirupathi": {
        "rating": 4.4,
        "phone": "+91 8321098765",
        "timings": "8:00 AM - 8:00 PM",
        "address": "Tiruchanoor Road, Tirupathi, Andhra Pradesh"
    },
    "Bangalore": {
        "rating": 4.6,
        "phone": "+91 7210987654",
        "timings": "8:00 AM - 9:00 PM",
        "address": "MG Road, Bangalore, Karnataka"
    }
}

# Vehicle issues and solutions
VEHICLE_ISSUES = {
    "air conditioner": {
        "causes": ["Low refrigerant", "Faulty compressor", "Clogged filters"],
        "solutions": ["Recharge AC refrigerant 🔄", "Replace compressor if needed 🛠", "Clean or replace air filters 🧹"]
    },
    "engine": {
        "causes": ["Low oil level", "Faulty spark plugs", "Fuel system issues"],
        "solutions": ["Check and top up engine oil ⛽", "Replace spark plugs 🔌", "Clean fuel injectors 🚿"]
    },
    "tires": {
        "causes": ["Underinflation", "Worn tread", "Alignment issues"],
        "solutions": ["Inflate to recommended PSI 💨", "Replace tires if worn out 🔄", "Get wheel alignment done 🛞"]
    },
    "overheating": {
        "causes": ["Low coolant", "Faulty thermostat", "Radiator blockage"],
        "solutions": ["Top up coolant 🧊", "Replace thermostat 🌡", "Flush radiator system 🚿"]
    },
    "brakes": {
        "causes": ["Worn brake pads", "Low brake fluid", "Rotor damage"],
        "solutions": ["Replace brake pads 🛑", "Top up brake fluid ⚠", "Resurface or replace rotors 🔄"]
    }
}

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "language" not in st.session_state:
    st.session_state.language = "English"
if "app_rating" not in st.session_state:
    st.session_state.app_rating = None
if "show_tools" not in st.session_state:
    st.session_state.show_tools = False
if "cart" not in st.session_state:
    st.session_state.cart = []
if "username" not in st.session_state:
    st.session_state.username = "User"

# Sidebar for settings
with st.sidebar:
    st.markdown("## ⚙ Settings")
    
    # Language selection
    st.session_state.language = st.selectbox(
        "Language 🌐",
        ["English", "Hindi"],
        key="lang_select"
    )
    
    # App rating
    st.session_state.app_rating = st.slider(
        "Rate our app ⭐",
        1, 5, 3,
        key="rating_slider"
    )
    
    # Tools catalog toggle
    if st.button("🛠 Tools Catalog"):
        st.session_state.show_tools = not st.session_state.show_tools
    
    # External website link
    st.markdown("---")
    st.markdown("### Partner Services")
    st.markdown("[GoMechanic](https://gomechanic.in) 🔗")

# Header with logo
st.markdown("""
<div class="header">
    <h1>🚗 Vehicare</h1>
    <p>Your Vehicle Assistant</p>
</div>
""", unsafe_allow_html=True)

# Time-based greeting
current_hour = datetime.now().hour
if 5 <= current_hour < 12:
    greeting = "Good morning! ☀"
elif 12 <= current_hour < 17:
    greeting = "Good afternoon! 🌤"
elif 17 <= current_hour < 21:
    greeting = "Good evening! 🌙"
else:
    greeting = "Hello! 🌃"

# Username input
if len(st.session_state.messages) == 0:
    st.session_state.username = st.text_input("Please enter your name:")
    if st.session_state.username:
        st.session_state.messages.append({
            "role": "assistant", 
            "content": f"{greeting} {st.session_state.username}! I'm Vehicare, your vehicle assistant. How can I help you today? 🚗💨"
        })

# Tools catalog page
if st.session_state.show_tools:
    st.markdown("## 🛠 Tools Catalog")
    
    # Sample tools data
    tools = [
        {"name": "Engine Oil", "price": 599, "image": "https://m.media-amazon.com/images/I/61X9Z5Z5Z5L.SL1500.jpg"},
        {"name": "Air Filter", "price": 349, "image": "https://m.media-amazon.com/images/I/61X9Z5Z5Z5L.SL1500.jpg"},
        {"name": "Brake Pads", "price": 899, "image": "https://m.media-amazon.com/images/I/61X9Z5Z5Z5L.SL1500.jpg"},
        {"name": "Spark Plugs", "price": 249, "image": "https://m.media-amazon.com/images/I/61X9Z5Z5Z5L.SL1500.jpg"},
    ]
    
    # Display tools
    cols = st.columns(2)
    for i, tool in enumerate(tools):
        with cols[i % 2]:
            st.image(tool["image"], width=150)
            st.markdown(f"{tool['name']}** - ₹{tool['price']}")
            if st.button(f"Add to Cart 🛒", key=f"add_{i}"):
                st.session_state.cart.append(tool)
                st.success(f"Added {tool['name']} to cart!")
    
    # Cart section
    st.markdown("---")
    st.markdown("## 🛒 Your Cart")
    if st.session_state.cart:
        total = sum(item["price"] for item in st.session_state.cart)
        for item in st.session_state.cart:
            st.markdown(f"- {item['name']} (₹{item['price']})")
        st.markdown(f"Total: ₹{total}")
        
        if st.button("Proceed to Booking"):
            st.success("Booking confirmed! Thank you for your purchase. 🎉")
            st.session_state.cart = []
    else:
        st.info("Your cart is empty. Add some tools!")
    
    if st.button("Back to Chat"):
        st.session_state.show_tools = False
        st.experimental_rerun()

# Chat interface
else:
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    
    # User input
    user_input = st.chat_input("Describe your vehicle issue...")
    
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Check for greetings
        greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
        # if any(greet in user_input.lower() for greet in greetings):
        if False:
            response = f"{greeting} {st.session_state.username}! How can I assist you with your vehicle today? 🚗"
        
        # Check for vehicle issues
        elif any(issue in user_input.lower() for issue in VEHICLE_ISSUES.keys()):
            issue_found = None
            for issue in VEHICLE_ISSUES.keys():
                if issue in user_input.lower():
                    issue_found = issue
                    break
            
            causes = "\n- ".join(VEHICLE_ISSUES[issue_found]["causes"])
            solutions = "\n- ".join(VEHICLE_ISSUES[issue_found]["solutions"])
            
            response = f"""I understand you're having {issue_found} issues. Here's what might be wrong: 🔍

Possible Causes:
- {causes}

Recommended Solutions:
- {solutions}

Would you like to book a service appointment? 🛠"""
            
            # Add service booking prompt
            st.session_state.ask_for_booking = True
        
        # Check for service booking confirmation
        elif "book" in user_input.lower() or "appointment" in user_input.lower():
            response = "Here are some nearby service stations: 🏢\n\n"
            for location, details in SERVICE_STATIONS.items():
                response += f"""{location}** ⭐ {details['rating']}
📞 {details['phone']}
🕒 {details['timings']}
📍 {details['address']}

"""
            response += "Please reply with the location you'd like to book at. 📍"
            st.session_state.ask_for_location = True
        
        # Handle location selection for booking
        elif st.session_state.get("ask_for_location"):
            selected_location = None
            for location in SERVICE_STATIONS.keys():
                if location.lower() in user_input.lower():
                    selected_location = location
                    break
            
            if selected_location:
                response = f"""Booking confirmed at {selected_location}! ✅

Details:
📞 {SERVICE_STATIONS[selected_location]['phone']}
🕒 {SERVICE_STATIONS[selected_location]['timings']}
📍 {SERVICE_STATIONS[selected_location]['address']}

Thank you for using Vehicare! 🚗💨"""
                st.session_state.ask_for_location = False
            else:
                response = "I couldn't identify that location. Please try again with one of these: " + ", ".join(SERVICE_STATIONS.keys())
        
        # Non-vehicle related queries
        else:
            response = "I'm sorry, I only respond to vehicle-related issues. 🚗 Please ask me about your car problems!"
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()