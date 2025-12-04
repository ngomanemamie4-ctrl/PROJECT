import random


def main():
    target_num = random.randint(0, 10)
    while True:
        try:
            guess = int(input("Guess a number between 0-10: "))
            if guess < target_num:
                print("Chosen number is too low.")
            elif guess > target_num:
                print("Chosen number is too high.")
            else:
                print("Numbers Match! You won!")
                break
        except (ValueError):
            print("Error: Please enter a valid integer.")
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled. Exiting.")
            break


if __name__ == "__main__":
    main()
