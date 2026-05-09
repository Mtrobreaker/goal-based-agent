import json
import os


class TaskManager:

    def __init__(self):

        self.file_path = "data/progress.json"

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump({}, file)

    def save_progress(self, goal, completed_tasks):

        data = self.load_progress()

        data[goal] = completed_tasks

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_progress(self):

        with open(self.file_path, "r") as file:
            return json.load(file)