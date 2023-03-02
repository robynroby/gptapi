import requests
import sqlite3

# API endpoint for the OpenAI API
api_endpoint = "https://api.openai.com/v1/engines/text-davinci-002/jobs"

# API Key for the OpenAI API
api_key = "YOUR_API_KEY"

# Connect to the SQLite database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Send a request to the OpenAI API
def send_request(text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": text,
        "max_tokens": 100,
        "temperature": 0.5,
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    return response.json()

# Retrieve data from the SQLite database
def retrieve_data(query):
    cursor.execute(query)
    return cursor.fetchall()

# Example usage
text = "What is the capital of France?"
response = send_request(text)
answer = response["choices"][0]["text"]
print(answer)

query = "SELECT name FROM cities WHERE country = 'France'"
result = retrieve_data(query)
print(result)
