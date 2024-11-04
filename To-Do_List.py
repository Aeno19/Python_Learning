to_do_list = []
# Function to add a task
def add_task(task):
    to_do_list.append(task)
    print(f'Task "{task}" has been added successfully to the to-do list.')
def delete_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f'Task "{task}" has been removed successfully from the to-do list.')
    else:
        print(f'Error. Task "{task}" not found in the to-do list.')
def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(to_do_list, start=1):
            print(f"{idx}. {task}")
while True:
    print("To-Do List Options:")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View all tasks")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to delete: ")
        delete_task(task)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Error. Please try again.")