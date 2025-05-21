
from flask import Flask, request, jsonify
from pyngrok import ngrok
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome! Your chatbot is running. Try /test?message=Hello"

# Test route
@app.route("/test", methods=["GET"])
def test():
    message = request.args.get('message', 'Hello')
    return jsonify({"response": f"You said: {message}"})

# Webhook route for Twilio
@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'hello' in incoming_msg or 'hi' in incoming_msg:
        msg.body("Hi there! 👋 I'm your chatbot.")
    else:
        msg.body("Sorry, I didn’t understand that. Try saying 'hello'.")

    return str(response)

# Run Flask app + ngrok
if __name__ == '__main__':
    # Open an ngrok tunnel to the Flask app
    tunnel = ngrok.connect(5000)
    print(" * Ngrok tunnel available at:", tunnel.public_url)
    print(f" * Use this URL for your webhook: {tunnel.public_url}/webhook")
    print(" * Test your bot at:", tunnel.public_url + "/test?message=Hello")

    # Start Flask app
    app.run(port=5000)
