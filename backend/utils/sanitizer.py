def detect_language(text: str) -> str:
    for char in text:
        if '\u1000' <= char <= '\u109F':  # Myanmar Unicode range
            return "my"
    return "en"