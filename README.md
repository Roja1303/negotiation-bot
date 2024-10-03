# negotiation-bot
"A negotiation bot API built using Google Generative AI for dynamic price negotiation scenarios. This bot can process customer messages and respond with tailored counteroffers to simulate a negotiation process."


# Negotiation Bot API

## Overview
The Negotiation Bot is an API designed to assist in negotiating product prices between suppliers and customers. The bot utilizes Google AI Studio's generative model to provide contextual responses based on user input.

## Table of Contents
- [Installation](#installation)
- [Integration of the Model](#integration-of-the-model)
- [API Endpoints](#api-endpoints)
- [Example Requests](#example-requests)

## Installation

### Prerequisites
- Python 3.7 or higher
- `venv` for creating a virtual environment (optional but recommended)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/negotiation_bot.git
   cd negotiation_bot

**2: Create a virtual environment (optional):**

python -m venv venv

**3:Activate the virtual environment:**

-  For Windows:
     venv\Scripts\activate
-  For macOS/Linux:
     source venv/bin/activate

 **4:Install the required dependencies:**

      pip install google-generative-ai flask

**5:Set your API key:** In your terminal, set the environment variable for your API key:

      export API_KEY='YOUR_API_KEY'  # For macOS/Linux
      set API_KEY='YOUR_API_KEY'     # For Windows PowerShell






**INTEGRATION OF THE MODEL**
The model is integrated using the google-generative-ai package. The bot listens for HTTP POST requests to negotiate prices. Upon receiving a request, it generates a response based on the user's message and the current price of the product.

The main function to interact with the model is get_negotiation_response, which constructs a prompt and calls the generative model to fetch a suitable response.







**API ENDPOINTS
POST /negotiate**
This endpoint accepts negotiation requests and returns a response from the bot.


**Request Format**
Headers:
Content-Type: application/json
Body:json

{
    "offer": <YOUR_OFFER>,
    "message": "<YOUR_MESSAGE>"
}

**Response Format**
The response will include:

bot_response: The bot's reply to the user's message.
current_price: The current price of the product






**EXAMPLE REQUEST**
**i used cURL** OR even you can use **POSTMAN**
To interact with your negotiation bot using the command prompt, you can use cURL commands :

**Step 1: Open Command Prompt**
          Press Win + R, type cmd, and press Enter.
**Step 2: Navigate to Your Project Directory**
          Use the cd command to change your directory to the project folder where your bot is located. For example:
             ** cd C:\Users\user\PycharmProjects\negotiation_bot**
**Step 3: Use cURL to Send Requests**
          You can send POST requests to your bot using cURL. The format for the command is as follows:
          
**SYNTAX::      curl -X POST http://127.0.0.1:5000/negotiate -H "Content-Type: application/json" -d "{\"offer\": <YOUR_OFFER>, 
                     \"message\": \ <YOUR_MESSAGE\"}"**
                  
    "offer": <YOUR_OFFER>,(offer you need type here)
    "message": "<YOUR_MESSAGE>"(message you wanted to ask )

**example**:   **  curl -X POST http://127.0.0.1:5000/negotiate -H "Content-Type: application/json" -d "{\"offer\": 150, \"message\": 
                 \"I would like to buy this product at a lower price.\"}"**




**Conclusion**
This README provides the necessary steps to set up and use the Negotiation Bot API. For any questions or issues, please feel free to reach out through the project's GitHub page.


### Instructions to Use This Template
1. Replace `https://github.com/yourusername/negotiation_bot.git` with the actual URL of your GitHub repository.
2. Replace `YOUR_API_KEY` with a placeholder text that indicates where to input the API key.
3. Adjust any sections as needed to match the specifics of your project, such as details in the overview, the integration section, or example requests and responses. 

After completing the README, save it as `README.md` in the root of your GitHub repository. This will help others understand how to set up and use your negotiation bot effectively!




