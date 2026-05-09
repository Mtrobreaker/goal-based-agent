from agent.agent import GoalBasedAgent
from agent.processor import clean_input, extract_goal

agent = GoalBasedAgent()

print("Real Goal-Based Agent Started!")

while True:

    user_input = input("\nYou: ")

    cleaned = clean_input(user_input)

    if cleaned == "exit":
        break

    elif cleaned == "progress":

        print(agent.show_progress())

    else:

        goal = extract_goal(cleaned)

        if goal:
            print(agent.set_goal(goal))
        else:
            print("I could not understand your goal.")