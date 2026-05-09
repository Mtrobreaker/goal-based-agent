from agent.memory import Memory
from agent.planner import Planner
from agent.task_manager import TaskManager


class GoalBasedAgent:

    def __init__(self):

        self.memory = Memory()
        self.planner = Planner()
        self.task_manager = TaskManager()

    def set_goal(self, goal):

        self.memory.set_goal(goal)

        plan = self.planner.generate_plan(goal)

        if not plan:
            return "I don't know this goal yet."

        self.task_manager.save_progress(goal, [])

        response = "\n".join(
            [f"Step {i+1}: {task}" for i, task in enumerate(plan)]
        )

        return f"Goal Set: {goal}\n\nPlan:\n{response}"

    def show_progress(self):

        goal = self.memory.get_goal()

        if not goal:
            return "No active goal."

        progress = self.task_manager.load_progress()

        completed = progress.get(goal, [])

        return f"Completed Tasks:\n{completed}"