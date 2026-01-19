#step1: understand goal
#step2: identify potential problems
#step3: come up with solutions to fix problems
#step4: plan what actions to do
#step5: execute


assignment = {"tasks": ["identify goal", "analyze data", "execute"]}
goal = "all done"
tries = 0

def plan(assignment):
    return assignment["tasks"]

def execute(action, assignment):
    global tries
    print(f"executing: {action}")
    if action == "execute" and tries == 0:
        print("failed to execute")
        tries += 1
        return False
    assignment["tasks"].remove(action)
    return True

while assignment["tasks"]:
    actions = plan(assignment)
    i = 0
    while i < len(actions):
        action = actions[i]
        success = execute(action, assignment)
        if not success:
            print(f"replanning {action}")
            break
        i += 1
print("all tasks completed")