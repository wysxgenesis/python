def add(a, b): 
    return a + b
def minus(a, b): 
    return a - b
def multiply(a, b): 
    return a * b
def divide(a, b): 
    return a / b

def calc():
    while True:
        ask = input("do you want to add, subtract, multiply or divide: ")
        if ask == "add":
            a = int(input("what is the first number you want to add "))
            b = int(input("what is the second number you want to add "))
            result = add(a, b)
            print(result)
            break
        elif ask == "minus":
            a = int(input("what is the first number you want to subtract "))
            b = int(input("what is the second number you want to subtract "))
            result = minus(a, b)
            print(result)
            break
        elif ask == "multiply":
            a = int(input("what is the first number you want to multiply "))
            b = int(input("what is the second number you want to multiply "))
            result = multiply(a, b)
            print(result)
            break
        elif ask == "divide":
            a = int(input("what is the first number you want to divide "))
            b = int(input("what is the second number you want to divide "))
            result = divide(a, b)
            print(result)
            break
        else:
            print("answer using add, subtract, multiply or divide only")

while True:
    ask = input("do you want to use calculator (y/n) ")
    if ask == "y":
        print("ok")
        calc()
        break
    elif ask == "n":
        print("ok bye")
        break
    else:
        print("invalid answer")

