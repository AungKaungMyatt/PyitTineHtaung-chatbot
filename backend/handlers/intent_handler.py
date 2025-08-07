import json
import os
import re
from difflib import get_close_matches
import logging

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEYWORDS_PATH = os.path.join(BASE_DIR, "../data/intent_keywords.json")

with open(KEYWORDS_PATH, "r", encoding="utf-8") as f:
    intent_keywords = json.load(f)

def detect_language(text: str) -> str:
    for char in text:
        if '\u1000' <= char <= '\u109F':  # Myanmar Unicode range
            return "mm"
    return "en"

def detect_intent(user_input: str) -> str:
    user_input = user_input.lower().strip()
    lang = detect_language(user_input)

    for intent, keywords in intent_keywords.items():
        for keyword in keywords:
            keyword = keyword.lower().strip()
            if lang == "en":
                pattern = r'\b' + re.escape(keyword) + r'\b'
                if re.search(pattern, user_input):
                    return intent
            else:  # For Myanmar, use direct substring match
                if keyword in user_input:
                    return intent

    return "ai"
