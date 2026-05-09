from agent.goals import GOALS


class Planner:

    def generate_plan(self, goal):

        if goal in GOALS:
            return GOALS[goal]

        return []