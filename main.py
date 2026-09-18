from github_api import get_github_api, get_user, get_repository, search_users


def check_api():
    data = get_github_api()

    if data:
        print("\nAPI Status: 200")
        print("GitHub API is working.")
    else:
        print("\nAPI check failed.")


def find_user():
    username = input("\nEnter GitHub username: ").strip().lstrip("@")

    if not username:
        print("Username cannot be empty.")
        return

    user = get_user(username)

    if user:
        print("\n--- GitHub Profile ---")
        print("Username:", user.get("login"))
        print("Name:", user.get("name"))
        print("Public repos:", user.get("public_repos"))
        print("Followers:", user.get("followers"))
        print("Following:", user.get("following"))
        print("Profile:", user.get("html_url"))


def find_repository():
    owner = input("\nEnter repository owner: ").strip().lstrip("@")
    repo = input("Enter repository name: ").strip()

    if not owner or not repo:
        print("Owner and repository name cannot be empty.")
        return

    repository = get_repository(owner, repo)

    if repository:
        print("\n--- GitHub Repository ---")
        print("Name:", repository.get("name"))
        print("Full name:", repository.get("full_name"))
        print("Description:", repository.get("description"))
        print("Visibility:", repository.get("visibility"))
        print("Stars:", repository.get("stargazers_count"))
        print("Forks:", repository.get("forks_count"))
        print("Open issues:", repository.get("open_issues_count"))
        print("Default branch:", repository.get("default_branch"))
        print("Repository:", repository.get("html_url"))


def search_github_users():
    query = input("\nEnter search username: ").strip()

    if not query:
        print("Search query cannot be empty.")
        return

    users = search_users(query)

    if users is None:
        return

    if not users:
        print("No users found.")
        return

    print("\n--- Search Results ---")

    for number, user in enumerate(users[:10], start=1):
        print(f"{number}. {user.get('login')}")
        print(f"   Profile: {user.get('html_url')}")


def main():
    while True:
        print("\n========================")
        print("     GitHub API Tool")
        print("========================")
        print("1. Check API")
        print("2. Find GitHub User")
        print("3. Find Repository")
        print("4. Search GitHub Users")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            check_api()
        elif choice == "2":
            find_user()
        elif choice == "3":
            find_repository()
        elif choice == "4":
            search_github_users()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
