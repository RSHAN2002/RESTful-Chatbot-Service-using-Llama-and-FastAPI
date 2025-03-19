# RESTful-Chatbot-Service-using-Llama-and-FastAPI

"""

This project is a simple chatbot API built using Flask and the Groq library for AI-generated responses.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set the Groq API Key as an environment variable:
   ```bash
   export GROQ_API_KEY='your_api_key_here'  # On Windows use `set GROQ_API_KEY=your_api_key_here`
   ```

## Running the Application

To start the Flask server, run:
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/chatbot`.

## Testing the API

You can test the API using the provided `test_chat.py` script:
```bash
python test_chat.py
```

Alternatively, you can use Postman or `curl`:
```bash
curl -X POST http://127.0.0.1:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Hello!"}'
```

## Endpoints

### POST /chatbot
#### Request Body:
```json
{
  "message": "Your message here"
}
```
#### Response:
```json
{
  "response": "Chatbot's reply"
}
```

## License
This project is open-source and free to use.
"""
