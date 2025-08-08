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

    def get_tip(self, user_input: str, language: str = "en") -> str:
        user_input = user_input.lower()
        matches = get_close_matches(user_input, self.tips.keys(), n=1, cutoff=0.4)
        
        if matches:
            match = matches[0]
            return f"{self.tips[match]} (Banking Topic: {match})"

        fallback = {
            "en": "I couldn't find a specific banking tip, but always stay secure while banking online!",
            "my": "တိကျတဲ့ဘဏ်လုပ်ငန်းဆိုင်ရာအကြံဉာဏ်မတွေ့ပါ။ သို့သော် အွန်လိုင်းဘဏ်လုပ်ငန်းများကို အသုံးပြုသောအခါ အမြဲတမ်းလုံခြုံမှုရှိစေရန် သတိထားပါ။"
        }

        return fallback.get(language, fallback["en"])

'''import json
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
        return "I couldn't find a specific banking tip, but always stay secure while banking online!"'''