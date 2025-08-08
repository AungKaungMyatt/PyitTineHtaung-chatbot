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

    def get_tip(self, user_input: str, language: str = "en") -> str:
        user_input = user_input.lower()
        matches = get_close_matches(user_input, self.tips.keys(), n=1, cutoff=0.4)
        if matches:
            match = matches[0]
            tip_data = self.tips[match]
            if isinstance(tip_data, dict):
                return f"{tip_data.get(language, tip_data.get('en'))} (Topic: {match})"
            else:
                return f"{tip_data} (Topic: {match})"
        if language == "my":
            return "အကြံပြုချက်တစ်ခုမှ မတွေ့ရှိနိုင်ပါ။ သတိထားပြီး လုံခြုံမှုရှိအောင်နေပါ။"
        return "I couldn't find a specific tip, but always stay cautious and secure!"


'''import json
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
        return "I couldn't find a specific tip, but always stay cautious and secure!"'''