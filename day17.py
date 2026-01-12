try:
    num = int(input("enter a number: "))
    print(1/num)
except ZeroDivisionError:
    print("you cant divide by 0")
except ValueError:
    print("enter numbers only")
except Exception:
    print("something went wrong")