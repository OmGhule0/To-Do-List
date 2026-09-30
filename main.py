#TO DO LIST 
print("|---------------------------------|")
print("          TO-DO LIST ")
print("|---------------------------------|")

print("Welcome User :) to [To-Do List]")

#list to store tasks
tasks = []
status = []

while True:

#Main Menu

    print("\nWhat would you like to do?")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Search Task")
    print("7. Filter Tasks")
    print("8. Task Statistics")
    print("9. Exit")

    choice = input("\nEnter your choice: ").strip().lower()

    #OPTION 1 ADD TASK MENU

    if choice == "1" or choice == "add task":

        task = input("Enter your task: ").strip()

        if task == "":
            print("Task cannot be empty.")

        else:
            tasks.append(task)
            status.append("Pending")

            print("Task added successfully!")

    #OPTION 2 VIEW TASK MENU

    elif choice == "2" or choice == "view tasks":

        print("\n:-----------[ YOUR TASKS ] -----------:")

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i], "-", status[i])

        print(":---------------------------------:")
    
    
    #OPTION 3 UPDATE TASK MENU

    elif choice == "3" or choice == "update task":

        if len(tasks) == 0:
            print("No tasks available to update.")

        else:
            print("\n:-----------[ UPDATE TASK ] -----------:")

            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_number = input("\nEnter the task number to update: ")

            if task_number.isdigit():

                task_number = int(task_number)

                if task_number >= 1 and task_number <= len(tasks):

                    new_task = input("Enter the new task: ").strip()

                    if new_task == "":
                        print("Task cannot be empty.")

                    else:
                        tasks[task_number - 1] = new_task

                        print("Task updated successfully!")

                else:
                    print("Invalid task number.")

            else:
                print("Please enter a valid number.")

            print(":--------------------------------------:")


    #OPTION 4 DELETE TASK MENU

    elif choice == "4" or choice == "delete task":

        if len(tasks) == 0:
            print("No tasks available to delete.")

        else:
            print("\n:-----------[ DELETE TASK ] -----------:")

            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_number = input("\nEnter the task number to delete: ")

            if task_number.isdigit():

                task_number = int(task_number)

                if task_number >= 1 and task_number <= len(tasks):

                    deleted_task = tasks.pop(task_number - 1)
                    status.pop(task_number - 1)

                    print("Task deleted successfully!")
                    print("Deleted task:", deleted_task)

                else:
                    print("Invalid task number.")

            else:
                print("Please enter a valid number.")

            print(":--------------------------------------:")
            
    #OPTION 5 MARK TASK AS COMPLETED

    elif choice == "5" or choice == "mark task as completed":
        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\n:-------[ MARK TASK COMPLETED ]-------:")

            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i], "-", status[i])

            task_number = input("\nEnter the task number to complete: ")

            if task_number.isdigit():
                task_number = int(task_number)

                if task_number >= 1 and task_number <= len(tasks):

                    if status[task_number - 1] == "Completed":
                        print("Task is already completed.")

                    else:
                        status[task_number - 1] = "Completed"
                        print("Task marked as completed!")

                else:
                    print("Invalid task number.")

            else:
                print("Please enter a valid number.")

            print(":------------------------------------:")


    # OPTION 6 SEARCH TASK MENU

    elif choice == "6" or choice == "search task":

        if len(tasks) == 0:
            print("No tasks available to search.")

        else:
            print("\n:-----------[ SEARCH TASK ] -----------:")

            search_task = input("Enter task name to search: ").strip().lower()

            if search_task == "":
                print("Search cannot be empty.")

            else:
                found = False

                for i in range(len(tasks)):

                    if search_task in tasks[i].lower():

                        print(i + 1, ".", tasks[i], "-", status[i])

                        found = True

                if found == False:
                    print("Task not found.")

            print(":--------------------------------------:")

    # OPTION 7 FILTER TASK MENU

    elif choice == "7" or choice == "filter tasks":
        if len(tasks) == 0:
            print("No tasks available to filter.")

        else:
            print("\n:-----------[ FILTER TASKS ] -----------:")
            print("1. Show Pending Tasks")
            print("2. Show Completed Tasks")
            print("3. Show All Tasks")

            filter_choice = input("\nEnter your choice: ").strip().lower()

            if filter_choice == "1" or filter_choice == "pending":
                print("\n:-----------[ PENDING TASKS ] -----------:")

                found = False

                for i in range(len(tasks)):
                    if status[i] == "Pending":
                        print(i + 1, ".", tasks[i])
                        found = True

                if found == False:
                    print("No pending tasks.")

            elif filter_choice == "2" or filter_choice == "completed":
                print("\n:--------- [ COMPLETED TASKS ] ----------:")

                found = False

                for i in range(len(tasks)):
                    if status[i] == "Completed":
                        print(i + 1, ".", tasks[i])
                        found = True

                if found == False:
                    print("No completed tasks.")

            elif filter_choice == "3" or filter_choice == "all":
                print("\n:-------------[ ALL TASKS ] -------------:")

                for i in range(len(tasks)):
                    print(i + 1, ".", tasks[i], "-", status[i])

            else:
                print("Invalid filter choice.")

            print(":----------------------------------------:")

    #OPTION 8 TASK STATISTICS MENU

    elif choice == "8" or choice == "task statistics":
        print("\n:----------[ TASK STATISTICS ] ----------:")

        total_tasks = len(tasks)
        completed_tasks = status.count("Completed")
        pending_tasks = status.count("Pending")

        print("Total Tasks     :", total_tasks)
        print("Completed Tasks :", completed_tasks)
        print("Pending Tasks   :", pending_tasks)

        if total_tasks > 0:
            completion_percentage = (completed_tasks / total_tasks) * 100
            print("Completion      :", round(completion_percentage, 2), "%")
        else:
            print("Completion      : 0 %")

        print(":-----------------------------------------:")

    #OPTION 9 EXIT THE TO TO LIST MENU

    elif choice == "9" or choice == "exit":
        print("EXITED Successfully")
        break

    else:
        print("Invalid choice. Please try again.")
        

   