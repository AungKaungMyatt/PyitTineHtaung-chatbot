class BankingInfoHandler:
    def branch_hours(self, user_input: str, lang: str) -> str:
        if lang == "my":
            return (
                "ဘဏ်အချိန်ဇယားမှာ ဌာနခွဲပေါ်မူတည်ပြီး ကွာခြားနိုင်သည်။ "
                "တိကျသည့် အချိန်ကို သိချင်ပါက ဌာနခွဲနာမည် သို့မဟုတ် မြို့အမည်ကို ပြောပါ၊ "
                "မဟုတ်လျှင် ဘဏ်၏ တရားဝင် ဌာနခွဲရှာဖွေမူ ဝဘ်ဆိုက်ကို သုံးပါ။"
            )
        return (
            "Branch hours vary by location. Tell me the branch name or city and I can help, "
            "or use the bank’s official branch locator to confirm today’s hours."
        )
