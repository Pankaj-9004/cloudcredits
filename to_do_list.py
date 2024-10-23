# To-Do List Application

# List to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Exit")

# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks to display.")
    else:
        print("\nYour tasks:")
        for i in range(len(tasks)):
            status = "Completed" if tasks[i]['completed'] else "Not Completed"
            print(f"{i + 1}. {tasks[i]['title']} - {status}")

# Function to add a new task
def add_task():
    task_title = input("\nEnter the title of the new task: ")
    task = {'title': task_title, 'completed': False}
    tasks.append(task)
    print(f"Task '{task_title}' added.")

# Function to mark a task as completed
def mark_task_completed():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Task '{tasks[task_num - 1]['title']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        print("Exiting the To-Do List application.")
        break
    else:
        print("Invalid option. Please try again.")
