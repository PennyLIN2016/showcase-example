import os, json

class PromptManager:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), 'main.prompty')
        try:
            with open(path, 'r') as f:
                self.prompts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.prompts = {}

    def update_prompts(self, filepath):
        with open(filepath, 'r') as file:
            self.prompts = json.load(file)

    def save_prompts(self, filepath):
        with open(filepath, 'w') as file:
            json.dump(self.prompts, file)

    def get_prompt(self, key):
        return self.prompts.get(key, "Prompt not found.")

    def add_prompt(self, key, prompt):
        self.prompts[key] = prompt

    def remove_prompt(self, key):
        if key in self.prompts:
            del self.prompts[key]