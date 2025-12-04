def main():
    students = {}  # {name: [grades]}
    
    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Add student")
        print("2. Add grade to student")
        print("3. View student average")
        print("4. View all students")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            name = input("Enter student name: ").strip()
            if name:
                if name not in students:
                    students[name] = []
                    print(f"Student '{name}' added.")
                else:
                    print(f"Student '{name}' already exists.")
            else:
                print("Error: Name cannot be empty.")
        
        elif choice == '2':
            name = input("Enter student name: ").strip()
            if name in students:
                try:
                    grade = float(input("Enter grade (0-100): "))
                    if 0 <= grade <= 100:
                        students[name].append(grade)
                        print(f"Grade {grade} added to '{name}'.")
                    else:
                        print("Error: Grade must be between 0 and 100.")
                except ValueError:
                    print("Error: Please enter a valid number.")
            else:
                print(f"Student '{name}' not found.")
        
        elif choice == '3':
            name = input("Enter student name: ").strip()
            if name in students:
                if students[name]:
                    avg = sum(students[name]) / len(students[name])
                    print(f"'{name}' average: {avg:.2f}")
                else:
                    print(f"'{name}' has no grades yet.")
            else:
                print(f"Student '{name}' not found.")
        
        elif choice == '4':
            if students:
                for name in students:
                    if students[name]:
                        avg = sum(students[name]) / len(students[name])
                        print(f"  {name}: {avg:.2f} (grades: {len(students[name])})")
                    else:
                        print(f"  {name}: No grades yet")
            else:
                print("No students added yet.")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
