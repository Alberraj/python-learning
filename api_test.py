from github_api import get_github_api


data = get_github_api()

if data:
    print("Status: 200")
    print("GitHub API:")
    print(data["current_user_url"])
    print(data["user_url"])
    print(data["repository_url"])
    print("API test completed successfully!")
else:
    print("API test failed.")
