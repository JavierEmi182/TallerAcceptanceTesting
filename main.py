from functions import *
#Initialize task list
tasklist = {"complete":[],"incomplete":[],"cancelled":[]}

def menuTD(tasklist):
    selection = ""
    while selection != "E":
        print("\nPlease select one option: ")
        print("1. Add a new task to the list")
        print("2. List all the tasks in the list")
        print("3. Order the tasks by certain criteria")
        print("4. Mark a task as completed")
        print("5. Mark a task as cancelled")
        print("6. Exit")
        selection = input("Enter your option: ")
        if selection == "1":
            taskname = input("Please enter the name of the task you want to add: ")
            addTask(taskname)
        elif selection == "2":
            listTasks(tasklist)
        elif selection == "3":
            orderList(tasklist)
        elif selection == "4":
            completeTask(tasklist,1)
        elif selection == "5":
            completeTask(tasklist,2)
        else:
            #Exits the program
            selection = "E"
            return 

def addTask(task):
    tasklist["incomplete"].append(task)
    print("\nTask %s added."%task)
    return

def listTasks(tasklist):
    list_task = tasklist["complete"] + tasklist["incomplete"] + tasklist["cancelled"]
    if checkEmpty(list_task):
            return
    for status in tasklist.keys():
        print("%s tasks: "%status.capitalize())
        for num,task in enumerate(tasklist[status]):
            print("%d. %s"%(num+1,task.capitalize()))
    return 
            
def completeTask(tasklist,status):
    if checkEmpty(tasklist["incomplete"]):
            return
    if status == 1:
        print("Select the task you want to mark as completed.")
    elif status == 2:
        print("Select the task you want to mark as cancelled.")
    for tid,task in enumerate(tasklist["incomplete"]):
            print("%d. %s"%(tid+1,task))
    taskInput = input("Enter the number of the task: ")
    while not taskInput.isdigit():
        print("Incorrect input (Must be a number).")
        taskInput = input("Enter the number of the task: ")
    taskInput = int(taskInput) - 1
    while not taskInput < len(tasklist["incomplete"]):
            print("Incorrect number, please enter a number in the list.")
            taskInput = input("Enter the number of the task: ")
            while not taskInput.isdigit():
                print("Incorrect input (Must be a number).")
                taskInput = input("Enter the number of the task: ")
            taskInput = int(taskInput) - 1
    if status == 1:
        print("\nMarked as complete the task: %s"%tasklist["incomplete"][taskInput])
        tasklist["complete"].append(tasklist["incomplete"][taskInput])
    elif status == 2:
        print("\nMarked as cancelled the task: %s"%tasklist["incomplete"][taskInput])
        tasklist["cancelled"].append(tasklist["incomplete"][taskInput])
    del tasklist["incomplete"][taskInput]
    return



def clearList(tasklist):
    print("\nTasklist cleared.")
    tasklist["complete"] = []
    tasklist["incomplete"] = []
    return

def orderList(tasklist):
    #This function pretends to order the tasklist according to some criteria.
    print("Select the criteria to order the taskList: ")
    print("1. Alphabetical order")
    print("2. Completed tasks")
    print("3. Not complete tasks")
    print("4. Cancelled tasks")
    selection = input("Please enter the number of the criteria you would like to order the list: ")
    while not selection.isdigit():
        print("Incorrect input. Please enter a number.")
    selection = int(selection)
    if selection == 1:
        list_task = tasklist["complete"] + tasklist["incomplete"] + tasklist["cancelled"]
        list_task.sort()
        for num,elem in enumerate(list_task):
            print("%d. %s "%(num+1,elem))
    elif selection == 2:
        for num,elem in enumerate(tasklist["complete"]):
            print("%d. %s"(num+1,elem))
    elif selection == 3:
        for num,elem in enumerate(tasklist["incomplete"]):
            print("%d. %s"(num+1,elem))
    elif selection == 4:
        for num,elem in enumerate(tasklist["cancelled"]):
            print("%d. %s"(num+1,elem))
    else:
        print("Incorrect input.")
    return

def checkEmpty(list_task):
    if len(list_task) <= 0:
        print("List is empty.")
        return True
    return False
    

print("To Do List Manager")
menuTD(tasklist)