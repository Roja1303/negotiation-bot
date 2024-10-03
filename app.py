from flask import Flask, request, jsonify
import os
import google.generativeai as genai

# Create the Flask app
app = Flask(__name__)

# Configure the API key
genai.configure(api_key=os.environ["API_KEY"])


# Function to interact with Google AI Studio for negotiation
def get_negotiation_response(user_message, current_price):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Specify the model

    # Prepare the prompt
    prompt = f"You are a supplier. The customer says: '{user_message}'. Your current price is {current_price}. Negotiate a better price or provide a counteroffer."

    # Generate content using the model
    response = model.generate_content(prompt)

    # Return the response text
    return response.text if response else "Sorry, I couldn't understand your request."


# Define the negotiation route
@app.route('/negotiate', methods=['POST'])
def negotiate():
    data = request.get_json()
    offer = data.get('offer')
    message = data.get('message')

    # Current price for negotiation (you can set this to your desired value)
    current_price = 500  # Example current price, adjust as needed

    # Get the bot's response
    bot_response = get_negotiation_response(message, current_price)

    # Prepare the response data
    response_data = {
        'bot_response': bot_response,
        'current_price': current_price
    }

    # Return the response as JSON
    return jsonify(response_data)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
