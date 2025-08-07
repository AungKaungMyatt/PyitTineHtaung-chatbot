from handlers.rule_engine.password_checker import PasswordChecker
from handlers.rule_engine.tip_handler import TipHandler
from handlers.rule_engine.scam_detector import ScamDetector
from handlers.rule_engine.banking_handler import BankingTipHandler
from handlers.rule_engine.greeting_handler import GreetingHandler
#from handlers.intent_handler import detect_intent

def detect_language(text: str) -> str:
    # Basic Unicode-based detection
    for char in text:
        if '\u1000' <= char <= '\u109F':  # Myanmar Unicode range
            return "mm"
    return "en"

class ChatBot:
    def __init__(self):
        self.password_checker = PasswordChecker()
        self.tip_handler = TipHandler()
        self.scam_detector = ScamDetector()
        self.banking_handler = BankingTipHandler()
        self.greeting_handler = GreetingHandler()
        # self.ai_responder = LLMResponder()

    def get_response(self, user_input: str, intent: str) -> str:
        language = detect_language(user_input)

        if intent == "tip":
            return self.tip_handler.get_tip(user_input, language)
        elif intent == "banking_tip":
            return self.banking_handler.get_tip(user_input, language)
        elif intent == "password_check":
            return self.password_checker.check(user_input, language)
        elif intent == "scam_check":
            return self.scam_detector.detect(user_input, language)
        elif intent == "greeting":
            return self.greeting_handler.respond(user_input, language)
        else:
            if language == "mm":
                return "ဤမေးခွန်းအတွက် AI ဖြေကြားမှုကို မကြာမီ ထည့်သွင်းမည်။"
            else:
                return "I couldn’t find a rule-based answer. An AI-generated answer will be added soon."

    '''def get_response(self, message: str) -> str:
        intent = self.detect_intent(message)

        if intent == "password_check":
            return self.password_checker.check(message)
        elif intent == "tip":
            return self.tip_handler.get_tip(message)
        elif intent == "scam_check":
            return self.scam_detector.detect(message)
        elif intent == "banking":
            return self.banking_handler.handle(message)
        else:
            return "Sorry, I couldn't understand that. Please try again."'''