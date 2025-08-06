'''import json
from pathlib import Path
from difflib import get_close_matches

class TipHandler:
    def __init__(self):
        # Load tips from JSON
        path = Path("data/tips.json")
        with open(path, "r", encoding="utf-8") as file:
            self.tips = json.load(file)

    def find_best_tip(self, user_input: str) -> str:
        user_input = user_input.lower()
        best_match = get_close_matches(user_input, self.tips.keys(), n=1, cutoff=0.3)
        if best_match:
            return f"{self.tips[best_match[0]]} (Tip topic: {best_match[0]})" #return tips[best_match[0]]
        return "Sorry, I don't have a tip for that specific question. Try asking differently!" '''

import json
import os
from difflib import get_close_matches

class TipHandler:
    def __init__(self, tip_file='data/tips.json'):
        self.tips = self.load_tips(tip_file)

    def load_tips(self, tip_file):
        if os.path.exists(tip_file):
            with open(tip_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return {}

    def get_tip(self, user_input: str) -> str:
        user_input = user_input.lower()
        matches = get_close_matches(user_input, self.tips.keys(), n=1, cutoff=0.4)
        if matches:
            match = matches[0]
            return f"{self.tips[match]} (Topic: {match})"
        return "I couldn't find a specific tip, but always stay cautious and secure!"
