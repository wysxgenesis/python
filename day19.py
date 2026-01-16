class Student:

    class_prob = 0      

    def __init__(self, revision_time, desired_score):
        self.revise = revision_time
        self.score = desired_score
    
    def check(self):
        Student.class_prob += self.revise
        if Student.class_prob == 0:
            print("you did not revise at all, put in my effort")
        elif 1<Student.class_prob<=9:
            print("you revised a little, keep it up")
        else:
            print("you are revising alot, maybe take a break?")

    def predict(self):
        if self.score == 100:
            factor = 0.75
        elif self.score >= 75:
            factor = 0.85
        elif self.score >= 50:
            factor = 0.95
        else:
            print("aim higher")

        chance = self.revise * factor
        chance = min(chance, 9.9)  
        print(f"you studied for {self.revise} hours this week")
        print(f"your chance of scoring {self.score} is {chance}")

        
        

student1 = Student(10, 60)
student1.check()
