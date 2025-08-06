class PasswordChecker:
    def check(self, pwd: str) -> str:
        if len(pwd) < 8:
            return "Your password is too short. Use at least 8 characters."
        if not any(c.isupper() for c in pwd):
            return "Add at least one uppercase letter."
        if not any(c.islower() for c in pwd):
            return "Add at least one lowercase letter."
        if not any(c.isdigit() for c in pwd):
            return "Add at least one number."
        if not any(c in "!@#$%^&*" for c in pwd):
            return "Add a special character (!@#$%^&*)"
        return "Strong password!"