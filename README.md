# 🚗 VehiCare AI Chatbot

## 🤖 AI-Powered Vehicle Assistance System

VehiCare is an AI-powered vehicle assistance chatbot developed using **Python, Streamlit, and Google Gemini API**.

The chatbot helps users understand common vehicle problems, provides troubleshooting guidance, suggests maintenance solutions, helps locate available service centers, assists with service appointment requests, recommends useful videos, and provides emergency roadside assistance information.

The main objective of VehiCare is to provide users with a simple and interactive platform for getting initial guidance about vehicle-related problems.

---

## 📸 Application Preview

![VehiCare Chatbot](VehiCare%20Project%20Photos/VehiCare%20Chatbot.png)

VehiCare provides an interactive chatbot interface where users can describe their vehicle problems and receive AI-powered assistance.

---

## ✨ Key Features

### 1. 🚗 Vehicle Assistance

VehiCare allows users to interact with the chatbot and ask questions related to their vehicles.

![Introducing VehiCare](VehiCare%20Project%20Photos/Introducing.png)

Users can ask about vehicle maintenance, engine problems, mileage issues, tire concerns, warning lights, and other common vehicle-related problems.

---

### 2. 🔧 Vehicle Problem Analysis

Users can describe their vehicle problem in natural language.

![User Problem](VehiCare%20Project%20Photos/User%20Problem.png)

The chatbot analyzes the user's problem and provides relevant information and possible troubleshooting guidance.

---

### 3. 🩺 Possible Causes

VehiCare provides possible causes related to the reported vehicle issue.

![Possible Causes](VehiCare%20Project%20Photos/Possible%20Causes.png)

For example, when a vehicle is overheating, the chatbot can explain possible causes such as:

- Low coolant level
- Radiator fan failure
- Thermostat problems
- Water pump failure
- Clogged radiator
- Head gasket problems

---

### 4. 📚 Additional Diagnostic Information

VehiCare can provide additional information related to the user's specific vehicle problem.

![Extra Information](VehiCare%20Project%20Photos/Extra%20Info%20About%20the%20User%20Problem.png)

This section can include symptoms to observe, maintenance information, and preventive tips.

---

### 5. 📍 Service Center Locator

Users can ask VehiCare to find available service centers in a particular location.

![Available Service Centers](VehiCare%20Project%20Photos/Available%20Service%20Centers.png)

The chatbot provides available service-center information including location and services.

---

### 6. 📅 Service Appointment Assistance

VehiCare assists users in providing the information required for a service appointment request.

![Book a Service Appointment](VehiCare%20Project%20Photos/Book%20a%20Service%20Appointment.png)

The user can provide details such as:

- Full Name
- Contact Number
- Vehicle Registration Number
- Preferred Date and Time
- Specific Vehicle Concern

---

### 7. ✅ Service Appointment Summary

After the user provides the required information, VehiCare displays a summary of the appointment request.

![Service Appointment Summary](VehiCare%20Project%20Photos/Service%20Appointment%20Summary.png)

The summary contains important information such as the customer name, vehicle, service center, preferred date and time, and reported issue.

---

### 8. 🎥 Video Recommendations

VehiCare can suggest useful video resources related to vehicle maintenance and troubleshooting.

![Video Recommendation](VehiCare%20Project%20Photos/Suggesting%20a%20suitable%20Video.png)

These recommendations can help users understand basic maintenance procedures and troubleshooting steps.

---

### 9. 🤝 Partner Services

The application provides access to partner services that can provide additional vehicle-related assistance.

![Partner Services](VehiCare%20Project%20Photos/Partner%20Services.png)

---

### 10. ⭐ Chatbot Rating

Users can rate their experience with the VehiCare chatbot.

![Chatbot Rating](VehiCare%20Project%20Photos/Chatbot%20Rating.png)

The rating feature helps collect user feedback about the chatbot experience.

---

## 🛠️ Technologies Used

- **Python** – Application development and backend logic
- **Streamlit** – Web application interface
- **Google Gemini API** – AI-powered conversational assistance
- **JSON** – Service-center and video data storage
- **HTML/CSS** – Interface customization
- **Git** – Version control
- **GitHub** – Source code and project hosting

---

## 📂 Project Structure

```text
VehiCare-AI-ChatBot/
│
├── app.py
├── app_v1.py
├── chatbot.py
├── chatbot_v1.py
├── config.py
├── requirements.txt
├── service_centers.json
├── videos.json
├── README.md
│
└── VehiCare Project Photos/
    ├── Available Service Centers.png
    ├── Book a Service Appointment.png
    ├── Chatbot Rating.png
    ├── Extra Info About the User Problem.png
    ├── Introducing.png
    ├── Partner Services.png
    ├── Possible Causes.png
    ├── Service Appointment Summary.png
    ├── Suggesting a suitable Video.png
    ├── User Problem.png
    └── VehiCare Chatbot.png
