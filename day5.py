def score_calc():
    sub = input("what subject is this for ")
    num = int(input("how many papers for this subject "))

    if num == 1:
        total1 = int(input("total score of paper 1: "))
        print()
        print(f"paper 1 is out of {total1}")
        print()
        score1 = int(input("input score of paper 1: "))
        print()
        result =(score1)/(total1) * 100
        print(f"you scored {result:.2f}% for {sub}")

    if num == 2:
        total1 = int(input("total score of paper 1: "))
        total2 = int(input("total score of paper 2: "))
        print()
        print(f"paper 1 is out of {total1}")
        print(f"paper 2 is out of {total2}")
        print()
        score1 = int(input("input score of paper 1: "))
        score2 = int(input("input score of paper 2: "))
        print()
        result =(score1 + score2)/(total1 + total2) * 100
        print(f"you scored {result:.2f}% for {sub}")

    if num == 3:
        total1 = int(input("total score of paper 1: "))
        total2 = int(input("total score of paper 2: "))
        total3 = int(input("total score for paper 3: "))
        print()
        print(f"paper 1 is out of {total1}")
        print(f"paper 2 is out of {total2}")
        print(f"paper 3 is out of {total3}")
        print()
        score1 = int(input("input score of paper 1: "))
        score2 = int(input("input score of paper 2: "))
        score3 = int(input("input score of paper 3: "))
        print()
        result =(score1 + score2 + score3)/(total1 + total2 + total3) * 100
        print(f"you scored {result:.2f}% for {sub}")
    
    if result >= 50:
        print("you passed")
    else:
        print("you failed")
    
while True:
    qns = input("do you want to calculate your marks (yes/no) ")
    if qns == "yes":
        score_calc()
        break
    elif qns == "no":
        continue
    else:
        print("please answer yes or no only")


