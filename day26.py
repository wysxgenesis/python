class Agent:
    def __init__(self):
        self.response = []
        self.review = []
        
    def prompt(self, input):
        response = f"thoughts on input {input}"
        self.response.append(response)
        return response
    
    def check(self):
        self.review.clear()
        if self.response == []:
            print("no prompt to check")
            return []
        for answer in self.response:
            split = answer.split()
            if len(split) < 5:
                review = "prompt is too short"
            else:
                review = ("prompt is ok")
            self.review.append({"response": answer, "review": review})
        print(review)
        return self.review
    
    def reflect(self):
        for ans in self.review:
            if ans["review"] != "prompt is ok":
                print(f"improve prompt {ans['response']}")
            else:
                print("no improvements needed")

