def mark():
    if marks >= 80:
        print("good job, continue to study hard")
    elif marks >= 50:
        print("you passed, but there is room for improvement")
    else:
        print("you failed, dont give up and study harder")

def advice():
    if marks >= 80:
        print("check work properly and revise more")
    elif marks >= 50:
        print("practise weaker concepts more and revise consistently")
    else:
        print("ensure foundation is good by revising and practising more")    

name = input("what is your name: ")

while True:
    sub = input(f"hello {name} what subject do you want to check: (math/science) ")
    if sub == "math" or sub == "science":
        break
    else:
        print("please answer yes or no only")

while True:
    marks = int(input(f"what is your marks for {sub}: (out of 100) "))
    if marks > 100:
        print("type in your marks as a percentage out of 100")
    else:
        break

mark()
while True:
    ask = input("do you want advice: (yes/no) ")
    if ask == "yes":
        advice()
        break
    elif ask == "no":
        print("ok")
        break
    else:
        print("please answer yes or no only")



