tasks_list = {}

next_tasks_id = 1

checkmark = "\u2713"

    


def add_task():
    global next_tasks_id 
    task_name = input('Enter the name of the task you wish to add to the list. ')
    completion = "Incomplete"
    tasks_list[next_tasks_id] = {"task name" : task_name, "Completion" : completion }
    print(f'Task #{next_tasks_id}: "{task_name}" added to checklist ')
    next_tasks_id += 1

def view_tasks():
    if not tasks_list:
        print("No tasks for right now!")
        return
    
    for tasks_id, task in tasks_list.items():
        status = f" {checkmark} Completed" if task["Completion"] == "Completed" else "Incomplete"
        print(f'Task #{tasks_id}: "{task["task name"]}"  Status: {status}')
        

def complete():
    if not tasks_list:
        print("No Tasks for now! Come back later!")
        return
    try:
        task_ids = input("Enter task numbers you wish to mark as completed (separate with spaces):\n")
        task_ids = [int(task_id) for task_id in task_ids.split()]
    except ValueError:
        print("Please enter valid task numbers separated by spaces.")
        return
    updated = False
    for task_id in task_ids:
        if task_id in tasks_list:
            tasks_list[task_id]["Completion"] = "Completed"
            print(f"Task #{task_id}: {tasks_list[task_id]["task name"]} Now {checkmark} {tasks_list[task_id]["Completion"]} ")
            updated = True
        else:
            print(f"Task #{task_id} not found.")
    if not updated:
        print("No valid tasks were marked as completed.")
    

def remove_tasks():
    try:
        option = int(input("Enter choose an option \n 1.) Delete task by task # \n 2.) Delete all completed tasks \n"))
    except ValueError:
        print("Please select option 1 or option 2")
        return
    if option == 1:
        try:
            task_id = int(input("Choose a task by # for deletion. "))
        except ValueError:
            print("Please input a valid task #")
        if task_id in tasks_list:
            print(f"Task #{task_id}: {tasks_list[task_id]["task name"]} Deleted Successfully ")
            del tasks_list[task_id]
            
        else:
            print("Task not found.")
    elif option == 2:
        completed_tasks = [task_id for task_id, task in tasks_list.items() if task["Completion"] == "Completed"]
        if not completed_tasks:
            print("No completed tasks found.")
            return
        for task_id in completed_tasks:
            task_name = tasks_list[task_id]["task name"]
            del tasks_list[task_id]
            print(f"Task #{task_id}: '{task_name}' deleted successfully.")
    else:
        print("Invalid option. Please select 1 or 2.")
    



def Main():
    while True:
        print("\nPlease choose an option:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task(s)")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete()
        elif choice == "4":
            remove_tasks()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


        
Main()