import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API from .env file
api_key = os.getenv("API_KEY")

api_key = "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"
endpoint = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

question = "how many continents are there?"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "inputs": question,
    "parameters": {
        "max_new_tokens": 100
    }
}

response = requests.post(endpoint, json=data, headers=headers)

try:
    response.raise_for_status()
    output = response.json()
    generated_text = output[0]["generated_text"]
    answer = generated_text.split("\n")[1]
    print(answer)
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
    print(f"Response content: {response.content}")

