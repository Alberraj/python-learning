import requests

url = "https://api.github.com/search/repositories"

params = {
    "q": "python",
    "per_page": 5
}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("Status:", response.status_code)
    print("Repositories found:", data["total_count"])
    print()

    for repo in data["items"]:
        print("Name:", repo["full_name"])
        print("Stars:", repo["stargazers_count"])
        print("URL:", repo["html_url"])
        print("-" * 40)

except requests.RequestException as e:
    print("Request error:", e)
except (KeyError, TypeError) as e:
    print("Response format error:", e)
