class CardHandler:
    def freeze_card(self, user_input: str, lang: str) -> str:
        if lang == "my":
            return (
                "ကတ်ပျောက်သို့မဟုတ် သံသယရှိပါက အဖွင့်စိတ်ချရမှုအတွက် အောက်ပါအဆင့်များလုပ်ဆောင်ပါ။"
                "1) ချက်ချင်းဘဏ်၏ တော့ခွန်းသို့ ခေါ်ဆိုပြီး ကတ်ပိတ်ရန်တင်ပြပါ။"
                "2) မည်သည့် လင့်ခ်များကိုမှ မနှိပ်ပါနှင့်။ OTP ကို မမျှဝေပါနှင့်။"
                "3) မည်သည့် အသုံးပြုမှုမမှန်ကန်မှုရှိပါက စာချုပ်တင်ပြပါ။"
                "မှတ်ချက်။ တော့ခွန်းနံပါတ်ကို ကတ်နောက်ဘက်တွင် ကြည့်ပါ။"
            )
        return (
            "If your card is lost or you suspect fraud, do this now:"
            "1) Call the bank hotline on the back of your card to request an immediate freeze."
            "2) Do not click any links or share OTP codes with anyone."
            "3) Report any unauthorized transactions to the bank."
            "Note: Always use the official hotline printed on your card."
        )
