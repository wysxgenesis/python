import json
class Agent:
    def __init__(self, goal):
        self.goal = goal
        self.memories = []
        self.data = "memory.json"

    def load_memories(self):
        try:
            with open(self.data, "r")as file:
                content = json.load(file)
                print(content)
        except FileNotFoundError:
            print("file not found")
            self.memories = []
    
    def ambition(self):
        print(f"your goal is {self.goal}")

    def add_memory(self):
        memory =  input("what are your memories: (type nil if no memories and separate each memory with comma)")
        if memory != "nil":
            new_memories = [m.strip() for m in memory.split(",")]
            self.memories.extend(new_memories)
            with open(self.data, "w") as file:
                json.dump(self.memories, file, indent=2)

    def reflect(self):
        if self.memories == []:
            print("you do not have any memories stored")
        else:
            print(f"you have {len(self.memories)} memories stored do you want to view them: (y/n)")
            ask = input()
            if ask == "y":
                try:
                    with open(self.data, "r")as file:
                        content = json.load(file)
                        print(content)
                except FileNotFoundError:
                    print("file not found")
                

            

