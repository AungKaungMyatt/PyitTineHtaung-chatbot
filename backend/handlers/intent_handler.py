import json
import os
from difflib import get_close_matches
import logging

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEYWORDS_PATH = os.path.join(BASE_DIR, "../data/intent_keywords.json")

with open(KEYWORDS_PATH, "r", encoding="utf-8") as f:
    INTENT_KEYWORDS = json.load(f)

def detect_intent(user_input: str) -> str:
    user_input = user_input.lower().strip()
    
    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            # Exact match or close similarity
            if keyword in user_input:
                return intent
            matches = get_close_matches(user_input, keywords, cutoff=0.8)
            if matches:
                return intent
            if keyword in user_input:
                logging.info(f"Intent '{intent}' matched by keyword '{keyword}'")
                return intent
    
    return "ai"