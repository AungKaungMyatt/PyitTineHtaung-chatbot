class PasswordChecker:
    def check(self, pwd: str, language: str = "en") -> str:
        messages = {
            "en": {
                "too_short": "Your password is too short. Use at least 8 characters.",
                "no_upper": "Add at least one uppercase letter.",
                "no_lower": "Add at least one lowercase letter.",
                "no_digit": "Add at least one number.",
                "no_special": "Add a special character (!@#$%^&*)",
                "strong": "Strong password!"
            },
            "my": {
                "too_short": "သင့်စကားဝှက်မှာ စာလုံး ၈ လုံးအထက်ရှိရန်လိုအပ်ပါသည်။",
                "no_upper": "အကြီးစာလုံးတစ်လုံးထည့်ပါ။",
                "no_lower": "အငယ်စာလုံးတစ်လုံးထည့်ပါ။",
                "no_digit": "နံပါတ်တစ်လုံးထည့်ပါ။",
                "no_special": "အထူးအက္ခရာ (!@#$%^&*) တစ်ခုထည့်ပါ။",
                "strong": "သင့်စကားဝှက်မှာလုံခြုံမှုကောင်းမွန်ပါသည်။"
            }
        }

        msg = messages.get(language, messages["en"])

        if len(pwd) < 8:
            return msg["too_short"]
        if not any(c.isupper() for c in pwd):
            return msg["no_upper"]
        if not any(c.islower() for c in pwd):
            return msg["no_lower"]
        if not any(c.isdigit() for c in pwd):
            return msg["no_digit"]
        if not any(c in "!@#$%^&*" for c in pwd):
            return msg["no_special"]
        return msg["strong"]
