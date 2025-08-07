class GreetingHandler:
    @staticmethod
    def respond(user_input: str, language: str = "en") -> str:
        greetings = {
            "en": {
                "response": "Hello, this is PyitTineHtaung Cyber Security Bot. How can I assist you today?",
                "keywords": ["hello", "hi", "hey", "greetings", "good morning", "good evening"]
            },
            "mm": {
                "response": "မင်္ဂလာပါ။ ပစ်တိုင်းထောင် Cyber Security chatbot မှ ကြိုဆိုပါတယ်။",
                "keywords": ["မင်္ဂလာပါ", "မင်္ဂလာ", "နေကောင်းလား"]
            }
        }

        # Get appropriate language set or fall back to English
        lang_set = greetings.get(language, greetings["en"])
        user_input_lower = user_input.lower()

        for keyword in lang_set["keywords"]:
            if keyword in user_input_lower:
                return lang_set["response"]

        # Default to English greeting if no keywords match
        return greetings["en"]["response"]
