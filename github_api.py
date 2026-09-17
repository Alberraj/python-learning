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


def get_user(username):
    url = f"{BASE_URL}/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print("User not found.")
            return None

        response.raise_for_status()
        return response.json()

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
