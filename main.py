from github_api import get_github_api, get_user


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


def main():
    while True:
        print("\n========================")
        print("     GitHub API Tool")
        print("========================")
        print("1. Check API")
        print("2. Find GitHub User")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            check_api()
        elif choice == "2":
            find_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
