import json
from datetime import datetime
import threading
import time
class Agent:
    def __init__(self):
        self.work = []
        self.data = "assignment.json"
        self.time_data = "worktime.json"
        self.time = []
        self.trigger = False
        self.night_owl = False
    def add_work(self):
        while True:
                try:
                    with open(self.data, "r") as file:
                            self.task = json.load(file)
                except FileNotFoundError:
                    self.work = []
                deadline = input("deadline(YYYY-MM-DD) for task: (type 0 if no deadline or type 'done' to exit) ")
                if deadline.lower() == "done":
                    break
                info = input("info: ")
                work_add = { 
                    "deadline": deadline,
                    "Task information": info
                }
                self.work.append(work_add)
                
        with open(self.data, "w") as file:
            json.dump(self.work, file, indent=2)

    def load_task(self):
        try:
            with open(self.data, "r") as file:
                self.work = json.load(file)
        except FileNotFoundError:
            print("no tasks stored")
            return

        print(f"you have {len(self.work)} tasks currently")
        ask2 = input(("do you want to view them(y/n): "))
        if ask2 == "y":
            try:
                with open(self.data, "r") as file:
                    self.work = json.load(file)
                    print(self.work)
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
    
    def reminders(self):
        try:
            with open(self.data, "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            print("No tasks found.")
            return
        try:
            with open(self.time_data, "r") as file:
                self.time = json.load(file)
        except FileNotFoundError:
            self.time = []
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

    def start_background_check(self):
        thread = threading.Thread(target=self.predict, daemon=True)
        thread.start()

    def predict(self):
        while True:
            if len(self.time) >= 3 and not self.trigger:
                times = [datetime.strptime(d["time you started work"], "%Y-%m-%d %H:%M:%S") for d in self.time]            
                current_time = datetime.strptime(self.time, "%Y-%m-%d %H:%M:%S")
                times.append(current_time)
                earliest = min(times)
                latest = max(times)
                mid = (latest + earliest)/2
                if (latest - earliest).total_seconds() <= 3600:
                    print(f"you tend to work around{mid} ")
                mid_min = mid.replace(second=0, microsecond=0)
                now = datetime.now().replace(second=0, microsecond=0)
                if now == mid_min:
                    print("you usually start work around this time, consider starting now")
                    self.trigger = True
                late = time(19, 0, 0)
                if mid >= late:
                    self.night_owl = True
            time.sleep(5)

    def productivity(self):
        try:
            with open(self.time_data, "r") as file:
                self.time = json.load(file)
        except FileNotFoundError:
            self.time = []
        print("enter 'start' when you are going to start your work")
        qns = input("enter: ").lower()
        if qns == "start":
            work_time = datetime.now().strftime("%H:%M:%S")
            start_times = {"time you started work": work_time}
            self.time.append(start_times)
            with open(self.time_data, "w") as file:
                json.dump(self.time, file, indent=2)
            print("work time recorded")
            self.triggered = False
        else:
            print("work not started")

        if self.night_owl == False:
            good_time_start = time(8, 0, 0)
            good_time_end = time(14, 0, 0)
            if not good_time_start <= work_time <= good_time_end:
                print("you might be working outside of productive hours, try working earlier")
        else:
            good_time = time(19, 0, 0)
            if not work_time >= good_time:
                print("you are night owl, but working late regularly is unhealthy, consider working earlier")
            

    def goals(self):
        qns2 = input("what is your goal: ").lower()
        if qns2 == "score" or qns2 == "marks" or qns2 == "exam":
            try:
                import day15
                day15.main()
            except Exception:
                print("something went wrong, reload and try again later")
        elif qns2 == "study" or qns2 == "plan" or qns2 == "studyplan":
            try:
                import day14
                day14.main()
            except Exception:
                print("something went wrong, reload and try again later")

