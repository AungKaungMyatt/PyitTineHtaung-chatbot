import json
import os
import re
from difflib import get_close_matches
import logging
from utils.sanitizer import detect_language

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEYWORDS_PATH = os.path.join(BASE_DIR, "../data/intent_keywords.json")

with open(KEYWORDS_PATH, "r", encoding="utf-8") as f:
    intent_keywords = json.load(f)

# Helper: normalize Myanmar text
def normalize_burmese_text(text: str) -> str:
    """Remove zero-width spaces and normalize spacing for Myanmar text."""
    text = text.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def detect_intent(user_input: str, lang: str | None = None):
    text = (user_input or "").strip()
    lang = lang or detect_language(text)

    text_lc = text.lower()
    if lang == "my":
        text_lc = normalize_burmese_text(text_lc)

    scores = {}
    matches = {}

    for intent, keywords in intent_keywords.items():
        score = 0.0
        hit_list = []
        for keyword in keywords:
            kw = keyword.lower().strip()
            if lang == "en":
                if re.search(r'\b' + re.escape(kw) + r'\b', text_lc):
                    score += 1.0
                    hit_list.append(kw)
            else:
                norm_kw = normalize_burmese_text(kw)
                if norm_kw in text_lc:
                    score += 1.0
                    hit_list.append(norm_kw)
        scores[intent] = score
        matches[intent] = hit_list

    # === tiny heuristics (domain-aware) ===
    # 1) Questions about phishing → banking_tip boost
    if any(q in text_lc for q in ["what should i do", "how do i", "what do i do", "what should we do"]):
        if any(p in text_lc for p in ["phishing", "smishing", "phishing sms", "phishing message"]):
            scores["banking_tip"] = scores.get("banking_tip", 0) + 1.5

    # 2) If user says "tip/tips/advice/recommendation" → boost tip
    if re.search(r"\b(tip|tips|advice|recommendation|best practice|best practices)\b", text_lc):
        scores["tip"] = scores.get("tip", 0) + 1.5

    # Pick highest score (tie-breaker: prefer scam_check > password_check > greeting > banking_tip > tip)
    priority = ["scam_check", "password_check", "greeting", "banking_tip", "tip"]
    best_intent = "ai"
    best_score = 0.0
    for intent in sorted(scores.keys(), key=lambda k: (scores[k], -priority.index(k) if k in priority else 99), reverse=True):
        if scores[intent] > best_score:
            best_intent = intent
            best_score = scores[intent]

    confidence = round(min(0.99, 0.4 + 0.1 * best_score), 3) if best_score > 0 else 0.60
    # Optional: log for debugging
    logging.info({"intent": best_intent, "score": best_score, "matches": matches.get(best_intent, [])})
    return best_intent, confidence

