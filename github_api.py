import requests


BASE_URL = "https://api.github.com"


def get_github_api():
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print("Request error:", e)
        return None


if __name__ == "__main__":
    data = get_github_api()

    if data:
        print("Status: 200")
        print("GitHub API:")
        print(data["current_user_url"])
        print(data["user_url"])
        print(data["repository_url"])
