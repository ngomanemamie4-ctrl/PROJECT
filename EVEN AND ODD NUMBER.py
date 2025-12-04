def main():
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
        return

    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


if __name__ == "__main__":
    main()