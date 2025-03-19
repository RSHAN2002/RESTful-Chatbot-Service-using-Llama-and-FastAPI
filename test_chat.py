import requests

# Define the API URL
api_url = "http://127.0.0.1:5000/chatbot"  # Update the URL if the Flask server is running elsewhere

# Define the request payload
test_payload = {
    "message": "What is LLM?"
}

# Send the POST request
test_response = requests.post(api_url, json=test_payload)

# Print the response
if test_response.status_code == 200:
    print("Chatbot Response:", test_response.json().get("response"))
else:
    print("Error:", test_response.json())