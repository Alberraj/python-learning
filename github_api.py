import requests

BASE_URL = "https://api.github.com"
TIMEOUT = 10


def get_github_api():
    try:
        response = requests.get(BASE_URL, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()

    except requests.Timeout:
        print("Request timed out.")
    except requests.ConnectionError:
        print("Connection error. Check your internet connection.")
    except requests.RequestException as e:
        print("Request error:", e)

    return None


def get_user(username):
    url = f"{BASE_URL}/users/{username}"

    try:
        response = requests.get(url, timeout=TIMEOUT)

        if response.status_code == 404:
            print("User not found.")
            return None

        if response.status_code == 429:
            print("Rate limit exceeded.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.Timeout:
        print("Request timed out.")
    except requests.ConnectionError:
        print("Connection error.")
    except requests.RequestException as e:
        print("Request error:", e)

    return None


def get_repository(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}"

    try:
        response = requests.get(url, timeout=TIMEOUT)

        if response.status_code == 404:
            print("Repository not found.")
            return None

        if response.status_code == 429:
            print("Rate limit exceeded.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.Timeout:
        print("Request timed out.")
    except requests.ConnectionError:
        print("Connection error.")
    except requests.RequestException as e:
        print("Request error:", e)

    return None


def search_users(query):
    url = f"{BASE_URL}/search/users"
    params = {"q": query}

    try:
        response = requests.get(url, params=params, timeout=TIMEOUT)

        if response.status_code == 429:
            print("Rate limit exceeded.")
            return None

        response.raise_for_status()
        return response.json().get("items", [])

    except requests.Timeout:
        print("Request timed out.")
    except requests.ConnectionError:
        print("Connection error.")
    except requests.RequestException as e:
        print("Request error:", e)

    return None
