# simple to do list to run in cmd

task=[]# a list to store our tasks

def menu():
    print("\n -------To DO list Menu -----")
    print("1.Add Task")
    print("2.View tools")
    print("3.Mark task as complete")
    print("4.Delet Task")
    print("5.Exit")
    
def add_task():
    task =input("Enter a new task:")
    task.append({"task":task , "done":False})
    print("Task added")
    
def view_task():
    if not task:
        print("No task yet.")
        return
    print("\n Your task:")
    for i , task in enumerate(task):
        status="Ok " if task["done"] else "Not ok"
        print(f"{i+1}.{task['task']}[{status}]")