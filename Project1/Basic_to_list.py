# -*- coding: utf-8 -*-
import os
import json

# file that store the task
TASKS_FILE = 'tasks.json'

# Load tasks from a JSON file and fix incorrect keys.
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
            # Fix any task that has wrong key1
            for task in tasks:
                if 'compeleted' in task:  # wrong key
                    task['completed'] = task.pop('compeleted')
                if 'completed' not in task:  # if missing
                    task['completed'] = False
            Save_tasks(tasks)  # save corrected version
            return tasks
    else:
        return [{"task": "Learn Python basics", "completed": False}]

# Save Task in the json file       
def Save_tasks(tasks):
  
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)


# Display Task from json file
def Display_tasks(tasks):
    if not tasks:
        print("There is not task Available")
    else:
        for index, task in enumerate(tasks,start = 1):
            status = "✔️" if task['completed'] else "❌"
            print(f"{index}. [{status}] {task['task']}")

# Add new task in json file
def Add_task(tasks):
    task_description = input("Enter the task: ")
    tasks.append({"task": task_description, "completed": False})
    Save_tasks(tasks)
    print("Task is added in the json file")

    
# Edit an existing task in the json file
def Edit_task(tasks):
    Display_tasks(tasks)
    task_number = int(input("Enter the task number to Edit: ")) - 1
    if 0 <= task_number < len(tasks):
        new_description = input("Enter the new task description: ")
        tasks[task_number]['task'] = new_description
        Save_tasks(tasks)
        print("Task updated fully.")
    else:
        print("Invalid task number.")
    

# Mark a task as completed in the json file
def Complete_task(tasks):
    Display_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        Save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.") 


# Delete a task from the json file
def Delete_task(tasks):
    Display_tasks(tasks)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        Save_tasks(tasks)
        print("Task deleted sucessfully.")
    else:
        print("Invalid task number.")

# Making the main function 
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Mark task as complete")
        print("5. Delete task")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            Display_tasks(tasks)
        elif choice == '2':
            Add_task(tasks)
        elif choice == '3':
            Edit_task(tasks)
        elif choice == '4':
            Complete_task(tasks)
        elif choice == '5':
            Delete_task(tasks)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Calling the main function 
if __name__ == "__main__":
    main()
