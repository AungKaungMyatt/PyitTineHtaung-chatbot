class ScamDetector:
    def __init__(self):
        self.scam_keywords = [
            "win", "prize", "claim", "click", "urgent", "lottery", "money", "free", "limited offer"
        ]

    def detect(self, message: str, language: str = "en") -> str:
        messages = {
            "en": {
                "scam": "This message might be a scam. Be cautious!",
                "safe": "No common scam phrases found. Be cautious anyway!"
            },
            "my": {
                "scam": "ဤမက်ဆေ့ချ်သည် အလိမ်အညာဖြစ်နိုင်ပါသည်။ သတိပြုပါ။",
                "safe": "သံသယဖြစ်ဖွယ်စကားလုံးများမတွေ့ပါ။ သတိပြုပါ။"
            }
        }

        msg = messages.get(language, messages["en"])

        lower_msg = message.lower()
        if any(keyword in lower_msg for keyword in self.scam_keywords):
            return msg["scam"]
        return msg["safe"]