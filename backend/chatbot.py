from handlers.rule_engine.password_checker import PasswordChecker
from handlers.rule_engine.tip_handler import TipHandler
from handlers.rule_engine.scam_detector import ScamDetector
from handlers.rule_engine.banking_handler import BankingTipHandler
from handlers.rule_engine.greeting_handler import GreetingHandler
from handlers.rule_engine.banking_info import BankingInfoHandler
from utils.sanitizer import detect_language  # Use the single source of truth

# from handlers.llm_responder import LLMResponder  # Uncomment when AI is ready

class ChatBot:
    """
    Rule-based multilingual chatbot for banking FAQs and tips.
    Falls back to AI-generated answers in the future when no rule matches.
    """

    def __init__(self) -> None:
        # Initialize all rule-based handlers
        self.password_checker = PasswordChecker()
        self.tip_handler = TipHandler()
        self.scam_detector = ScamDetector()
        self.banking_handler = BankingTipHandler()
        self.greeting_handler = GreetingHandler()
        self.banking_info = BankingInfoHandler()
        # self.ai_responder = LLMResponder()

    def get_response(self, user_input: str, intent: str) -> str:
        """
        Return the chatbot's response based on detected intent.

        Args:
            user_input (str): The user's query text.
            intent (str): The intent label detected by the intent handler.

        Returns:
            str: The chatbot's response text.
        """
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
        
        elif intent == "branch_hours":
            return self.banking_info.branch_hours(user_input, language)

        else:
            # Future: pass to AI responder
            # return self.ai_responder.generate(user_input, language)
            if language == "my":
                return "ဤမေးခွန်းအတွက် AI ဖြေကြားမှုကို မကြာမီ ထည့်သွင်းမည်။"
            else:
                return "I couldn’t find a rule-based answer. An AI-generated answer will be added soon."
