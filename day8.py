while True:
    ask = input("do you want to continue (y/n) ")
    if ask == "y":
        print("ok")
        print("hello world")
    elif ask == "n":
        print("ok bye")
        break
    else:
        print("invalid answer")