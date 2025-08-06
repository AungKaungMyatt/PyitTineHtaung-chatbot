class ScamDetector:
    def __init__(self):
        self.scam_keywords = ["win", "prize", "claim", "click", "urgent", "lottery", "money", "free", "limited offer"]

    def detect(self, message):
        lower_msg = message.lower()
        if any(keyword in lower_msg for keyword in self.scam_keywords):
            return "This message might be a scam. Be cautious!"
        return "No common scam phrases found. Be cautious anyway!"
