import json

files = "data24.json"
def store():
    try:
        with open(files, "r") as file:
            memory = json.load(file)
    except FileNotFoundError:
        memory = []
    data = input("enter data you want to store: ")
    memory.append(data)
    with open(files, "w") as file:
        json.dump(memory, file, indent=2)

def read():
    try:
        with open(files, "r") as file:
            content = json.load(file)
            print(content)
    except FileNotFoundError:
        print("file does not exist")

while True:
    ask = input("enter prompt: ").lower()
    if "input"in ask or "store" in ask:
        store()
        break
    elif "load" in ask or "read"in ask or "see" in ask:
        read()
        break
    else:
        print("agent cannot accomplish that yet")