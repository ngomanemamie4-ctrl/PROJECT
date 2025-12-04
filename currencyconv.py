def main():
    # Exchange rate: 1 USD = ~18.50 ZAR (approximate, can be updated)
    usd_to_rand = 18.50
    
    while True:
        print("\n--- Currency Converter (USD ↔ ZAR) ---")
        print("1. USD to Rand (ZAR)")
        print("2. Rand (ZAR) to USD")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            try:
                usd = float(input("Enter amount in USD: "))
                if usd < 0:
                    print("Error: Amount cannot be negative.")
                    continue
                rand = usd * usd_to_rand
                print(f"${usd:.2f} USD = R{rand:.2f} ZAR")
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '2':
            try:
                rand = float(input("Enter amount in Rand (ZAR): "))
                if rand < 0:
                    print("Error: Amount cannot be negative.")
                    continue
                usd = rand / usd_to_rand
                print(f"R{rand:.2f} ZAR = ${usd:.2f} USD")
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
