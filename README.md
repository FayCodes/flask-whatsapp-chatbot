# Automated Messaging Interface (Flask & Twilio) 🤖

### A production-ready WhatsApp integration service for automated user interaction and real-time response handling.

---

## 🛠 Overview
This repository contains a backend service built with **Flask** and the **Twilio Messaging API** to facilitate seamless communication between users and automated logic on WhatsApp. The system is designed to handle asynchronous webhooks and deliver context-aware responses.

## 🚀 Core Functionalities
- **Webhook Integration:** Leverages Twilio’s Programmable Messaging API to intercept incoming WhatsApp payloads.
- **Dynamic Routing:** A centralized message handler that parses user intent and routes logic based on predefined triggers.
- **Diagnostic Endpoint:** Includes a specialized `/test` route for health checks and service monitoring.
- **Cross-Platform Deployment:** Configuration support for local tunneling via **Ngrok** and cloud deployment on **Render** (via Procfile).

## 🧰 Tech Stack
- **Framework:** Flask (Python)
- **API Provider:** Twilio Messaging API
- **Deployment:** Render / Heroku (Production), Ngrok (Local Tunneling)
- **Protocol:** HTTP/POST via Webhooks

## 📂 System Architecture
1. **User** sends a message via WhatsApp.
2. **Twilio** receives the message and sends an HTTP POST request (Webhook) to the Flask app.
3. **App.py** processes the logic and returns a **TwiML** (Twilio Markup Language) response.
4. **Twilio** delivers the automated response back to the user's WhatsApp.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/FayCodes/flask-whatsapp-chatbot.git](https://github.com/FayCodes/flask-whatsapp-chatbot.git)
    ```
```bash
   pip install -r requirements.txt
```

**Configure Environment:**  
Set your Twilio Sandbox settings to point to your Ngrok or Render URL (e.g., https://your-url.com/whatsapp).

**Run the application:**

```bash
python app.py
```
**Developed by Faith Wafula | Lead Developer & Data Scientist**
