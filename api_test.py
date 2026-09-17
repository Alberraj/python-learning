import requests

url = "https://api.github.com"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("Status:", response.status_code)
    print("GitHub API:")
    print(data["current_user_url"])
    print(data["user_url"])
    print(data["repository_url"])

except requests.RequestException as e:
    print("Request error:", e)
except KeyError as e:
    print("JSON key not found:", e)

