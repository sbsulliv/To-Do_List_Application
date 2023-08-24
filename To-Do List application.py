import os

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        tasks = [task.strip() for task in file.readlines()]
else:
    tasks = []

def display_tasks():
   if not tasks:
       print("No tasks available.")
       return
   for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

def add_task(task):
    tasks.append(task)
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def mark_task_as_done(task_number):
    try:
        tasks.pop(task_number - 1)
        save_tasks()
    except IndexError:
        print("Incalid task number.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    while True:
        print("\nTo-Do List App")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            display_tasks()
            task_number = int(input("Enter the task number to mark as done:"))
            mark_task_as_done(task_number)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
    print("Bye!")