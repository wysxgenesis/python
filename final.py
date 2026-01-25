import json
from datetime import datetime
import time
import threading
restart = "restart.json"
class Agent:
    def __init__(self):
        self.work = []
        self.exam_list = []
        self.data = "exams.json"
        self.data2 = "tasks.json"
        self.data3 = "goals.json"
        self.task_list = []
        self.goal_list = []
        self.study = 1
        self.data4 = "assignment.json"
        self.time_data = "worktime.json"
        self.time = []
        self.trigger = False
        self.night_owl = False
        self.s = 1
        self.m = 3
        self.l = 5
        self.trigger2 = False

    def goals(self):
        resume["function"] = "goal"
        with open(restart, "w") as file:
            json.dump(resume, file)
        goal = input("enter goal(do not include time): ")
        goal_time = input("how long do you want to take to finish this: ").lower()
        goal_full = {
            "goal": goal,
            "time to finish": goal_time
        }
        self.goal_list.append(goal_full)
        print(f"in order to {goal} within {goal_time}, you can follow this plan")
        if "day" or "days" in goal_time:
            num_day = int(''.join(filter(str.isdigit, goal_time)))
            for i in range (1, (num_day+1)):
                self.task_list.append(f"day {i}: study/practise for {self.study} hours")
        elif "week" or "weeks" in goal_time:
            num_day = int(''.join(filter(str.isdigit, goal_time)))
            num_week = num_day * 7
            for i in range (1, (num_week+1)):
                self.task_list.append(f"day {i}: study/practise for {self.study} hours")
        elif "month" or "months" in goal_time:
            num_day = int(''.join(filter(str.isdigit, goal_time)))
            num_month = num_day * 30
            for i in range (1, (num_month+1)):
                self.task_list.append(f"day {i}: study/practise for {self.study} hours")
        with open(self.data2, "w") as file:
            json.dump(self.task_list, file, indent=2)
        with open(self.data3, "w") as file:
            json.dump(self.goal_list, file, indent=2)
    
    def load_goal(self):
        resume["function"] = "load goal"
        with open(restart, "w") as file:
            json.dump(resume, file)
        try:
            with open(self.data2, "r") as file:
                self.task_list = json.load(file)
        except FileNotFoundError:
            return
        try:
            with open(self.data3, "r") as file:
                self.goal_list = json.load(file)
        except FileNotFoundError:
            return
        while True:
            ask3 = input("what do you want to see(goal/task or type 'done' to exit): ")
            if ask3 == "goal":
                try:
                    print(self.goal_list)
                except FileNotFoundError:
                    print("file not found")
            elif ask3 == "task":
                try:
                    print(self.task_list)
                except FileNotFoundError:
                    print("file not found")
            elif ask3 == "done":
                print("exiting loop")
                break

    def exam_details(self):
        resume["function"] = "exam details"
        with open(restart, "w") as file:
            json.dump(resume, file)
        while True:
            exam = input("enter name of exam: ")
            sub = input("enter subject tested: ")
            when = input("enter day of exam(YYYY-MM-DD): ")
            ask = input("type 'done' to exit or type anything else to continue: ")
            if ask == "done":
                break
            exam_add = {
                "exam": exam,
                "subject": sub,
                "day of exam": when
            }
            self.exam_list.append(exam_add)

        with open(self.data, "w") as file:
            json.dump(self.goal_list, file, indent=2)

    def load_exam_details(self):
        resume["function"] = "load exam details"
        with open(restart, "w") as file:
            json.dump(resume, file)
        try:
            with open(self.data, "r") as file:
                self.exam_list = json.load(file)
        except FileNotFoundError:
            return
        
        ask2 = input("do you want to see exams(y/n): ")
        if ask2 == "y":
            try:
                print(self.exam_list)
            except FileNotFoundError:
                print("file not found")

    def add_work(self):
        resume["function"] = "add work"
        with open(restart, "w") as file:
            json.dump(resume, file)
        while True:
                try:
                    with open(self.data4, "r") as file:
                            self.task = json.load(file)
                except FileNotFoundError:
                    self.work = []
                deadline = input("deadline(YYYY-MM-DD) for task: (type 0 if no deadline or type 'done' to exit) ")
                if deadline.lower() == "done":
                    break
                info = input("info: ").lower()
                diff = input("difficulty:(easy/medium/hard): ").lower()
                work_add = { 
                    "deadline": deadline,
                    "Task information": info,
                    "difficulty": diff,
                    "urgency": 0
                }
                self.work.append(work_add)
                
        with open(self.data4, "w") as file:
            json.dump(self.work, file, indent=2)

    def load_task(self):
        resume["function"] = "load task"
        with open(restart, "w") as file:
            json.dump(resume, file)
        try:
            with open(self.data4, "r") as file:
                self.work = json.load(file)
        except FileNotFoundError:
            print("no tasks stored")
            return

        print(f"you have {len(self.work)} tasks currently")
        ask2 = input(("do you want to view them(y/n): "))
        if ask2 == "y":
            try:
                with open(self.data4, "r") as file:
                    self.work = json.load(file)
                    print(self.work)
            except FileNotFoundError:
                    print("file not found")

    def remove_task(self):
        resume["function"] = "remove task"
        with open(restart, "w") as file:
            json.dump(resume, file)
        while True:
            ask3 = input("are you sure you want to remove a task(y/n): ")
            if ask3 == "y":
                remove = input("enter task you want to remove: ")
                try:
                    with open(self.data4, "r") as file:
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
                with open(self.data4, "w") as file:
                    json.dump(task, file, indent=2)
                print("task deleted")
                break
            else:
                print("task not found")
    
    def reminders(self):
        resume["function"] = "reminders"
        with open(restart, "w") as file:
            json.dump(resume, file)
        try:
            with open(self.data4, "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            print("No tasks found.")
            return
        try:
            with open(self.time_data, "r") as file:
                self.time = json.load(file)
        except FileNotFoundError:
            self.time = []
        while True:
            now = datetime.now().date() 
            for task in tasks:
                deadline_str = task.get("deadline")
                if deadline_str == "0":
                    continue  
                try:
                    deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                except ValueError:
                    print(f"Invalid deadline format for task: {task.get('Task information')}")
                    continue
                if 0 <= (deadline_date - now).days <= 3:
                    task["urgency"] += self.l
                elif 4 <= (deadline_date - now).days <= 7:
                    task["urgency"] += self.m 
                else:
                    task["urgency"] += self.s

                diff_str = task.get("difficulty")
                if diff_str == "easy":
                    task["urgency"] += self.s
                elif diff_str == "medium":
                    task["urgency"] += self.m
                elif diff_str == "hard":
                    task["urgency"] += self.l
                
            max_urgency = max(task["urgency"] for task in tasks)
            impt_task = [task for task in tasks if task["urgency"] == max_urgency]
            if len(impt_task) == 1:
                print(f"the most urgent task is {impt_task[0]["Task information"]} with urgency level {impt_task[0]["urgency"]}")
            else:
                print("there are multiple tasks with highest urgency level")
                for task in impt_task:
                    print(f"- {task['Task information']} (urgency: {task['urgency']})")
            if self.trigger2 ==  True:
                print("you have started/completed one of the tasks in the task plan that helps you achieve your goals")
                print("thus, consider continuing with that task so that you still retain your previous knowledge")

    def start_background_check(self):
        resume["function"] = "start background check"
        with open(restart, "w") as file:
            json.dump(resume, file)
        thread = threading.Thread(target=self.predict, daemon=True)
        thread2 = threading.Thread(target=self.reminders, daemon=True)
        thread.start()
        thread2.start()

    def predict(self):
        resume["function"] = "predict"
        with open(restart, "w") as file:
            json.dump(resume, file)
        while True:
            if len(self.time) >= 3 and not self.trigger:
                times = [datetime.strptime(d["time you started work"], "%Y-%m-%d %H:%M:%S") for d in self.time]            
                current_time = datetime.strptime(self.time, "%Y-%m-%d %H:%M:%S")
                times.append(current_time)
                earliest = min(times)
                latest = max(times)
                mid = (latest + earliest)/2
                if (latest - earliest).total_seconds() <= 3600:
                    print(f"you tend to work around {mid} ")
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
        resume["function"] = "productivity"
        with open(restart, "w") as file:
            json.dump(resume, file)
        try:
            with open(self.time_data, "r") as file:
                self.time = json.load(file)
        except FileNotFoundError:
            self.time = []
        try:
            with open(self.data4, "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
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
            qns2 = input("what task are you doing(type 'achieving goal' if following task plan and type 'nil' if you are not doing the task you added): ").lower()
            for task in tasks:
                if qns2 == "nil" or tasks == []:
                    break
                elif qns2 == task["Task information"]:
                    task["urgency"] += 1
            if qns2 == "achieving goal":
                self.trigger2 = True
            else:
                self.trigger2 = False

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

    def feedback(self):
        resume["function"] = "feedback"
        with open(restart, "w") as file:
            json.dump(resume, file)
        qns = input("did the work session help(y/n): ").lower()
        if qns == "n":
            qns2 = input("was the timing of training plan bad or the reminders bad(timing/reminders): ").lower()
            if qns2 == "timing":
                qns3 = input("was it too long or too short(long/short): ").lower()
                if qns3 == "long":
                    self.study += 0.5
                    print("improvement made")
                elif qns3 == "short":
                    self.study -= 0.5
                    print("improvement made")
            elif qns2 == "reminders":
                qns4 = input("would you like values to be more spread out or closer together:(far/close): ").lower()
                if qns4 == "far":
                    self.s += 2
                    self.m += 3
                    self.l += 4
                    print("improvement made")
                elif qns4 == "close":
                    self.s -= 0.5
                    self.m -= 0.4
                    self.l -= 0.3
                    print("improvement made")

agent1 = Agent
try:
    with open(restart, "r") as file:
        resume = json.load(file)
except FileNotFoundError:
    resume = {"function": None}

if resume["function"] == "goal":
    agent1.goals()
if resume["function"] == "load goal":
    agent1.load_goal()
if resume["function"] == "exam details":
    agent1.exam_details()
if resume["function"] == "load exam details":
    agent1.load_exam_details()
if resume["function"] == "add work":
    agent1.add_work()
if resume["function"] == "load task":
    agent1.load_task()
if resume["function"] == "remove task":
    agent1.remove_task()
if resume["function"] == "reminders":
    agent1.reminders()
if resume["function"] == "start background check":
    agent1.start_background_check()
if resume["function"] == "predict":
    agent1.predict()
if resume["function"] == "productivity":
    agent1.productivity()
if resume["function"] == "feedback":
    agent1.feedback()

#call methods here:

