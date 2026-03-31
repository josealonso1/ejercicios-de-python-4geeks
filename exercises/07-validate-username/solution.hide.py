import re


def codeland_username_validation(text):
    if len(text) < 4 or len(text) > 25:
        return False
    if not text or not text[0].isalpha():
        return False
    if text.endswith("_"):
        return False
    if not re.fullmatch(r"[A-Za-z0-9_]+", text):
        return False
    return True


print(codeland_username_validation(input()))
