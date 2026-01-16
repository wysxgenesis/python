import json
from datetime import datetime
class Agent:
    def __init__(self):
        self.task = []
        self.data = "tasks.json"
        self.store =  "misc.json"
        self.storage = {}
    

    def add_task(self):
        while True:
                try:
                    with open(self.data, "r") as file:
                            self.task = json.load(file)
                except FileNotFoundError:
                    self.task = []
                deadline = input("deadline(YYYY-MM-DD) for task: (type 0 if no deadline or type 'done' to exit) ")
                if deadline.lower() == "done":
                    break
                info = input("info: ")
                task_add = { 
                    "deadline": deadline,
                    "Task information": info
                }
                self.task.append(task_add)
                
        with open(self.data, "w") as file:
            json.dump(self.task, file, indent=2)
            
    def load_task(self):
        try:
            with open(self.data, "r") as file:
                self.task = json.load(file)
        except FileNotFoundError:
            print("no tasks stored")
            return

        print(f"you have {len(self.task)} tasks currently")
        ask2 = input(("do you want to view them(y/n): "))
        if ask2 == "y":
            try:
                with open(self.data, "r") as file:
                    self.task = json.load(file)
                    print(self.task)
            except FileNotFoundError:
                    print("file not found")

    def remove_task(self):
        while True:
            ask3 = input("are you sure you want to remove a task(y/n): ")
            if ask3 == "y":
                remove = input("enter task you want to remove: ")
                try:
                    with open(self.data, "r") as file:
                        task = json.load(file)
                except FileNotFoundError:
                    print("task not found")
                    break
                found = False
                for element in task:
                    if element.get("info") == remove:
                        task.remove(element)
                        found = True
                        break
            if found:
                with open(self.data, "w") as file:
                    json.dump(task, file, indent=2)
                print("task deleted")
                break
            else:
                print("task not found")

    def misc_storage(self):
        key = input("enter a key to access your info: ")
        info = input("enter your info: ")
        self.storage = {
            key: info
        }
        try:
            with open(self.store, "x")as file:
                json.dump(self.storage, file, indent=2)
        except FileExistsError:
            print("file already created")
        
    def add_misc_storage(self):
        while True:
                key2 = input("key: (or type 'done' to exit) ")
                if key2.lower() == "done":
                    break
                info2 = input("info: ")
                self.storage[key2] = info2

    def view_storage(self):
        if self.storage == {}:
            print("file is empty")
        else:
            try:
                with open(self.store, "r")as file:
                    content = json.load(file)
                    print(content)
            except FileNotFoundError:
                print("file not found")

    def suggestions(self):
        try:
            with open(self.data, "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            print("No tasks found.")
            return
        
        if self.storage == {}:
            print("storage is empty, do you want to fill it up")
        elif self.task == []:
            print("you have no tasks added, do you want to add one")

        now = datetime.now().date() 
        for task in tasks:
            deadline_str = task.get("deadline")
            if deadline_str == "0":
                continue  
            try:
                deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            except ValueError:
                print(f"Invalid deadline format for task: {task.get('info')}")
                continue


            if 0 <= (deadline_date - now).days <= 5:
                print(f"Task '{task.get('info')}' is due on {deadline_str}, you might want to get started")
            

        



            
            

