# app.py - Flask backend for chatbot
# ---------------------------------
# This file creates a simple web server using Flask
# The server handles requests from the frontend (index.html)
# and sends chatbot responses back to the browser.

from flask import Flask, render_template, request, jsonify

# Create a Flask app instance
app = Flask(__name__)

# -------------------------------
# Function: chatbot_response
# -------------------------------
# Takes the user's input (a number 1–5) and returns
# the chatbot's response based on predefined options.
def chatbot_response(user_input):
    responses = {
        "1": "📦 Please enter your order number to check the status.",
        "2": "📍 Find a store: https://www.thewarehouse.co.nz/stores",
        "3": "❓ FAQs: https://help.thewarehouse.co.nz/",
        "4": "🎁 Gift Guide: https://www.thewarehouse.co.nz/c/gift-guide",
        "5": "💬 Connecting you to a live agent..."
    }
    # If user enters something else, return default warning
    return responses.get(user_input, "⚠️ Invalid option. Please type 1–5.")

# -------------------------------
# Route: Homepage
# -------------------------------
# When the user opens http://127.0.0.1:5000/
# Flask will render and return the index.html page.
@app.route("/")
def home():
    return render_template("index.html")

# -------------------------------
# Route: Chat (POST API)
# -------------------------------
# The frontend sends a POST request here with JSON {"message": "..."}.
# Flask extracts the user's message, gets a reply from chatbot_response(),
# and returns a JSON response {"reply": "..."}.
@app.route("/chat", methods=["POST"])
def chat():
    # Get JSON data from the request
    user_msg = request.json.get("message")
    # Generate bot reply using helper function
    bot_reply = chatbot_response(user_msg)
    # Send JSON back to the frontend
    return jsonify({"reply": bot_reply})

# -------------------------------
# Run the app
# -------------------------------
# When this file is run with "python app.py",
# the Flask development server will start on port 5000.
if __name__ == "__main__":
    app.run(debug=True)
