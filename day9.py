while True:
    task = input("what task do you have ")
    ask = input("do you have anymore tasks (y/n) ")
    if ask == "n":
        print("ok, exiting loop")
        break
    elif ask == "y":
        print("ok, restarting loop")
    else:
        print("answer using y or n only")

list = [task]
print("printing list of tasks...")
print(list)

while True:
    ask2 = input("do you want to input more tasks (y/n) ")
    if ask2 == "y":
        list.append(input("input tasks: "))
        break
    elif ask2 == "n":
        print("ok")
        break
    else:
        print("answer using y or n only")        

while True:
    ask3 = input("do you want to see all your tasks ")
    if ask3 == "y":
        print("printing tasks...")
        print(list)
        break
    elif ask3 == "n":
        print("ok")
        break
    else:
        print("answer using y or n only")