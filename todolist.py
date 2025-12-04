def to_do_list():
    tasks = []
    while True:
        print("\n1.Add task")
        print("2.View tasks")
        print("3.Remove task")
        print("4.Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            task = input("Enter a task: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
        elif choice == '2':
            if tasks:
                for task in tasks:
                    print("  - " + task)
            else:
                print("No tasks yet.")
        elif choice == '3':
            task = input("Enter task to remove: ").strip()
            if task in tasks:
                tasks.remove(task)
                print(f"Removed task: {task}")
            else:
                print("Task not found.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    to_do_list()

