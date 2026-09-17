import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    print("Warning: API_KEY is not configured.")

url = "https://api.github.com"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("Status:", response.status_code)
    print("API key loaded:", bool(api_key))
    print("GitHub API:")
    print(data["current_user_url"])
    print(data["user_url"])
    print(data["repository_url"])

except requests.RequestException as e:
    print("Request error:", e)
except KeyError as e:
    print("JSON key not found:", e)

print("API test completed successfully!")
