func = input("what do you want to do today (weather/time) ")
if func == "weather":
    print("the weather is sunny today")
elif func == "time":
    from datetime import datetime
    current = datetime.now()
    print(f"current time is {current}")