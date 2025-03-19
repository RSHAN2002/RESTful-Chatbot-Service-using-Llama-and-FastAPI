from flask import Flask, request
from flask_restful import Api, Resource
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from the config folder
load_dotenv(dotenv_path="config/.env")

application = Flask(__name__)
api_service = Api(application)

# Set your Groq API key (Store securely, use environment variables in production)
GROQ_API_KEY = os.getenv('GROQ_API_KEY')  # Replace with your actual API key
if not GROQ_API_KEY:
    raise ValueError("Groq API key is missing. Please set the GROQ_API_KEY variable.")

# Initialize the Groq client
groq_client = Groq(api_key=GROQ_API_KEY)

class ChatbotHandler(Resource):
    def post(self):
        """Chatbot endpoint to accept user messages and return LLaMA-generated responses."""
        try:
            request_data = request.get_json()
            user_input = request_data.get("message", "").strip()

            # Validate input
            if not user_input:
                return {"error": "Message cannot be empty"}, 400

            # Generate a response from LLaMA
            ai_response = groq_client.chat.completions.create(
                model="llama3-8b-8192",  # Using LLaMA-3 8B model
                messages=[{"role": "user", "content": user_input}]
            )

            # Extract and return the chatbot response
            chatbot_message = ai_response.choices[0].message.content
            return {"response": chatbot_message}, 200

        except Exception as error:
            return {"error": "An error occurred while processing your request."}, 500

# Add resources to the API
api_service.add_resource(ChatbotHandler, "/chatbot")

if __name__ == "__main__":
    application.run(debug=True)