# Simple To-Do List Program

tasks = []  # Empty list to store tasks

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
while True:
    show_menu()
    choice = input("Enter the number(1-4):")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ Task '{task}' added successfully!")

    elif choice == '2':
        print("\n📝 Your Tasks:")
        if not tasks:
            print("No tasks available!")
        else:
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task}")

    elif choice == '3':
        print("\n🗑 Remove a Task:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        task_no = int(input("Enter the task number to remove: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"❌ Task '{removed}' removed successfully!")
        else:
            print("Invalid task number!")

    elif choice == '4':
        print("👋 Exiting To-Do List. Goodbye!")
        break
        

    else:
        print("⚠️ Invalid choice! Please try again.")

