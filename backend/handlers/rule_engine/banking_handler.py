'''import json
import os
from difflib import get_close_matches

class BankingHandler:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        tips_path = os.path.join(base_dir, "../data/banking_tips.json")
        with open(tips_path, "r", encoding="utf-8") as f:
            self.tips = json.load(f)

    def handle(self, user_input: str) -> str:
        user_input = user_input.lower().strip()
        best_match = get_close_matches(user_input, self.tips.keys(), n=1, cutoff=0.5)
        if best_match:
            key = best_match[0]
            return f"{self.tips[key]} (Topic: {key})"
        return "Sorry, I couldn't find a relevant banking tip. Please rephrase your question."'''

import json
import os
from difflib import get_close_matches

class BankingTipHandler:
    def __init__(self, tip_file='data/banking_tips.json'):
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
            return f"{self.tips[match]} (Banking Topic: {match})"
        return "I couldn't find a specific banking tip, but always stay secure while banking online!"