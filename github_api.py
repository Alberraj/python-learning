import requests


BASE_URL = "https://api.github.com"
TIMEOUT = 10


def get_github_api():
    try:
        response = requests.get(BASE_URL, timeout=TIMEOUT)

        if response.status_code == 429:
            print("Rate limit exceeded. Please try again later.")
            return None

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
            print("Rate limit exceeded. Please try again later.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.Timeout:
        print("Request timed out.")
    except requests.ConnectionError:
        print("Connection error. Check your internet connection.")
    except requests.RequestException as e:
        print("Request error:", e)

    return None


if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip().lstrip("@")

    if not username:
        print("Username cannot be empty.")
    else:
        user = get_user(username)

        if user:
            print("\n--- GitHub Profile ---")
            print("Username:", user.get("login"))
            print("Name:", user.get("name"))
            print("Public repos:", user.get("public_repos"))
            print("Followers:", user.get("followers"))
            print("Following:", user.get("following"))
            print("Profile:", user.get("html_url"))
