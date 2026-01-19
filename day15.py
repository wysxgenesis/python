def main():
    mark_el = int(input("what are your english marks: "))
    mark_math = int(input("what are your math marks: "))
    mark_sci = int(input("what are your science marks: "))

    score = {"english": mark_el,
            "math": mark_math,
            "science": mark_sci}
    print(score)

    while True:
        ask = input("do you want to change any score(y/n): ")
        if ask == "y":
            ask2 = input("what subject marks do you want to change(english/math/science): ")
            if ask2 == "english":
                mark_el = int(input("new score: "))
                score.update({"english": mark_el})
                print(score)
                break
            elif ask2 == "math":
                mark_math = int(input("new score: "))
                score.update({"math": mark_math})
                print(score)
                break
            elif ask2 == "science":
                mark_sci = int(input("new score: "))
                score.update({"science": mark_sci})
                print(score)
                break
            else:
                print("that subject doesnt exist")

        elif ask == "n":
            break
        else:
            print("answer using y or n only")

    while True:
        ask3 = input("do you want to add a new subject and marks(y/n): ")
        if ask3 == "y":
            sub = input("subject: (or type 'done' to exit) ")
            if sub.lower() == "done":
                break
            mark_sub = int(input("marks: "))
            score[sub] = mark_sub
        elif ask3 == "n":
            break
        else:
            print("answer using y or n only")

    while True:
        ask4 = input("do you want to print score(y/n) ")
        if ask4 == "y":
            print(score)
            break
        elif ask4 == "n":
            break        
        else:
            print("answer using y or n only")