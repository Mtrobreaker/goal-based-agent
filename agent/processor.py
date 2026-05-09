# agent/processor.py

def clean_input(user_input: str) -> str:
    return user_input.lower().strip()


def extract_goal(user_input: str):

    goal_patterns = [
        "i want to become",
        "i want to",
        "my goal is",
        "goal:"
    ]

    for pattern in goal_patterns:

        if pattern in user_input:

            goal = user_input.replace(pattern, "").strip()

            break
    else:
        goal = user_input

    # 🔥 Goal normalization
    if "ai engineer" in goal and "become" not in goal:
        goal = "become ai engineer"

    if "web developer" in goal and "become" not in goal:
        goal = "become web developer"

    return goal