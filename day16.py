import json

mark_el = int(input("what are your english marks: "))
mark_math = int(input("what are your math marks: "))
mark_sci = int(input("what are your science marks: "))

score = {"english": mark_el,
         "math": mark_math,
        "science": mark_sci}
print(score)

json_data = score
files = "data.json"
try:
    with open(files, "x") as file:
        json.dump(score, file, indent = 2)
        print("json file created")
except FileExistsError:
    print("file already created")

def change_score():
    while True:
        ask = input("do you want to change any score(y/n): ")
        if ask == "y":
            ask2 = input("what subject marks do you want to change(english/math/science): ")
            if ask2 == "english":
                mark_el = int(input("new score: "))
                score.update({"english": mark_el})
                with open(files, "w") as file:
                    json.dump(score, file, indent = 2)
                print(score)
                break
            elif ask2 == "math":
                mark_math = int(input("new score: "))
                score.update({"math": mark_math})
                with open(files, "w") as file:
                    json.dump(score, file, indent = 2)
                print(score)
                break
            elif ask2 == "science":
                mark_sci = int(input("new score: "))
                score.update({"science": mark_sci})
                with open(files, "w") as file:
                    json.dump(score, file, indent = 2)
                print(score)
                break
            else:
                print("that subject doesnt exist")

        elif ask == "n":
            break
        else:
            print("answer using y or n only")

def add_score():
    while True:
        ask3 = input("do you want to add a new subject and marks(y/n): ")
        if ask3 == "y":
            sub = input("subject: (or type 'done' to exit) ")
            if sub.lower() == "done":
                break
            mark_sub = int(input("marks: "))
            score[sub] = mark_sub
            with open(files, "w") as file:
                json.dump(score, file, indent = 2)
                break
        elif ask3 == "n":
            break
        else:
            print("answer using y or n only")

def show_score():
    while True:
        ask4 = input("do you want to print score(y/n) ")
        if ask4 == "y":
            try:
                with open(files, "r")as file:
                    content = json.load(file)
                    print(content)
                    break
            except FileNotFoundError:
                print("file not found")
                break
        elif ask4 == "n":
            break        
        else:
            print("answer using y or n only")

while True:
    print("what do you want to do")
    print("type 1 to change score, type 2 to add subject and score, type 3 to view current score")
    ans = int(input("number: "))
    while True:
        if ans == "1":
            change_score()
            break
        elif ans == "2":
            add_score()
            break
        elif ans == "3":
            show_score()
            break
        else:
            print("use numbers 1, 2, 3 only")
    