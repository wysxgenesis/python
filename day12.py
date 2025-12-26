pts = 0

while True:
    goal = input("what goals do you have ")
    ask = input("do you have a study plan(y/n) ")
    if ask == "y":
        print("ok, exiting loop")
        break
    elif ask == "n":
        ask2 = input("ok, do you want to create a study plan(y/n) ")
        if ask2 == "y":
            print("ok, creating study plan...")
            break
        elif ask2 == "n":
            print("ok, exiting loop")
            break
        else:
            print("answer using y or n only")
    else:
        print("answer using y or n only")

if ask2 == "y":
    sub = input("what subject is this for ")
    task = input("what task do you want to complete ")
    times = float(input("how long do you want to study for(in hours only, only write numbers) "))
list = [sub, task, times]
print(f"task for the day: {list}")
print(f"your goals: {goal}")
marks = int(input(f"what is yor score for {sub} out of 100: "))
import datetime
fixed_time = datetime.datetime.now()

while True:
    import datetime
    now = datetime.datetime.now()
    if now >= (fixed_time + times):
        ask3 = input("are you done with your task(y/n) ")
        if ask3 == "y":
            print("good job")
            pts += 1
            break
        elif ask3 == "n":
            print("its ok, keep trying")
            pts += 0.5
            break
        else:
            print("answer using y or n only")
    else:
        time.sleep(60)
        continue

def goal_reach():
    while True:
        new_marks = int(input("what is your new marks for {sub}: (key in number or na if not applicable) "))
        if (new_marks - marks) >= 15:
            pts += 5
            break
        elif (new_marks - marks) >= 5:
            pts += 2.5
            break
        elif new_marks == "na":
            break
        else:
            print("answer using na or number only")
    
    if pts >= 25:
        print("good job, you have put in hard work and you are reaching your goals")
    elif pts > 10 and goal_reach <= 25:
        print("keep going, you are nearly there")
    else:
        print("dont give up")

def studyplan():
    while True:
        ask4 = input("do you want to update study plan (y/n) ")
        if ask4 == "y":
            ask5 = input("do you want to add to your current list or replace the current list(add, replace) ")
            while True:
                if ask5 == "add":
                    sub = input("what subject is this for ")
                    task= input("what task do you want to complete ")
                    times = float(input("how long do you want to study for(in hours only, only write numbers) "))
                    list.extend(sub, task, times)
                    print(list)
                    break
                elif ask5 == "replace":
                    sub = input("what subject is this for ")
                    task= input("what task do you want to complete ")
                    times = float(input("how long do you want to study for(in hours only, only write numbers) "))
                    list[0:3] = [sub, task, times]
                    print(list)
                    break
                else:
                    print("answer using add or replace only")
        elif ask4 == "n":
            print("ok")
            break
        else:
            print("answer using y or n only")

def goals():
    while True:
        ask6 = input("do you want to update goals (y/n) ")
        if ask6 == "y":
            ask7 = input("do you want to add to your current list or replace the current list(add, replace) ")
            while True:
                if ask7 == "add":
                    goal += input("what other goals do you have ")
                    print(goal)
                    break
                elif ask7 == "replace":
                    goal = input("what new goals do you have ")
                    print(goal)
                    break
                else:
                    print("answer using add or replace only")
        elif ask6 == "n":
            print("ok")
            break
        else:
            print("answer using y or n only")

def motiv():
    while True:
        if marks > 100:
            print("type in your marks as a percentage out of 100")
        else:
            break
    if marks >= 80:
        print("good job, continue to study hard")
    elif marks >= 50:
        print("you passed, but there is room for improvement")
    else:
        print("you failed, dont give up and study harder")

while True:
    print("what do you want to do")
    print("type 1 to see your goals, type 2 to see study plan, type 3 to get motivational quotes and type 4 to exit ")
    ask8 = int(input())
    if ask8 == 1:
        goals()
    elif ask8 == 2:
        studyplan()
    elif ask8 == 3:
        motiv()
    elif ask8 == 4:
        print("exiting loop")
        break
    else:
        print("only use 1, 2, 3 or 4 to answer")
if ask2 == "y":
    while True:
        import time
        days = 30
        hours = days * 24
        seconds = hours * 60 * 60
        time.sleep(seconds)
        goal_reach()