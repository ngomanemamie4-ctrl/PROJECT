def main():
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}°C = {fahrenheit:.2f}°F")
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5/9
                print(f"{fahrenheit}°F = {celsius:.2f}°C")
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
