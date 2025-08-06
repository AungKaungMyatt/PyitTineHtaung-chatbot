class GreetingHandler:
    @staticmethod
    def respond(user_input: str) -> str:
        if "mingalar" in user_input.lower() or "မင်္ဂလာပါ" in user_input:
            return "မင်္ဂလာပါ။ ပစ်တိုင်းထောင် Cyber Security chatbot မှ ကြိုဆိုပါတယ်။"
        else:
            return "Hello, this is PyitTineHtaung Cyber Security Bot. How can I assist you today?"
