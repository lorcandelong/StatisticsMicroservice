
import requests

def menu():
    print("\nWelcome to the Task Manager! \nChoose an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Edit tasks")
    print("4. Analytics")
    print("5. Help")
    print("6. Exit")

def help():
    print("\nHelp:")
    print(" Adding a task will prompt you to create a new task with a title and description. Viewing tasks  will show you your tasks along with their status. You can also view their description.")
    print(" Editing a task will allow you to modify the title, description, and status.")


def add_task(tasks):
    title = input("Enter the task Title: ")
    description = input("Enter the task Description: ")
    tasks.append({"Title": title, "Description": description, "completed": False})
    print(f"Task '{title}' added successfully! \nUse the Edit tasks menu to mark a task as completed or change details to keep track of your tasks.")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks, yay!")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "incomplete"
        print(f"{index + 1}. {task['Title']} - {status}")
    option = input("Would you like to view a description of a task? (input the task number or press enter to skip)")
    if option: 
        task_number = int(option)
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            print(f"Description of '{task['Title']}': {task['Description']}")
        
        
def edit_task(tasks):

    view_tasks(tasks)
    if not tasks:
        print("No tasks to edit.")

        return

    try:

        task_number = int(input("Enter the task number to edit: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            new_title = input(f"Enter new title (leave blank to keep '{task['Title']}'): ")
            new_description = input(f"Enter new description (leave blank to keep '{task['Description']}'): ")
            mark_completed = input("Warning: This will permamently change the status of a task until edited again. \nMark as completed? (y/n): ")

            while mark_completed.lower() not in ["y", "n"]:
                print("Invalid input. Please enter 'y' or 'n'.")
                mark_completed = input("Mark as completed? (y/n): ")

            task["completed"] = mark_completed.lower() == "y"

            if new_title:
                task["Title"] = new_title
            if new_description:
                task["Description"] = new_description

            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def analytics(tasks):

    try:
        response = requests.post(
            "http://localhost:5001/statistics",
            json={"tasks": tasks}
        )

        if response.status_code == 200:
            statistics = response.json()

            print("\nTask Statistics:")
            print(f"Total Tasks: {statistics['total_tasks']}")
            print(f"Completed Tasks: {statistics['completed_tasks']}")
            print(f"Incomplete Tasks: {statistics['incomplete_tasks']}")

        else:
            print("Unable to retrieve statistics.")

    except requests.exceptions.ConnectionError:
        print("Analytics service is unavailable. Please start the service.")


tasks = []

menu() 

input_choice = input("Enter option: ")

while input_choice != "6":
    if input_choice == "1":
        
        add_task(tasks)
    elif input_choice == "2":
        
        view_tasks(tasks)
    elif input_choice == "3":

        edit_task(tasks)
    elif input_choice == "4":
        
        analytics(tasks)
    elif input_choice == "5":
        help()
    else:
        print("Invalid option. Please try again.")

    menu()
    input_choice = input("Enter option: ")
