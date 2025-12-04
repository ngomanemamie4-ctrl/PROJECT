import getpass

# Declare password and username
correct_username = "Mamie"
correct_password = "12345"


def main():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled.")
            return

        if username == correct_username and password == correct_password:
            print("Login successful!")
            break
        else:
            attempts += 1
            print(f"Incorrect credentials. {max_attempts - attempts} attempts remaining.")
    else:
        print("Maximum attempts reached. Login failed.")


if __name__ == "__main__":
    main()