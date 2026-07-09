import re


def codeland_username_validation(text):
    # TODO: implement validation rules
    # 1) between 4 and 25 chars
    if not 4 <= len(text) <=25:
        return False 
    # 2) starts with a letter
    if not text or not text[0].isalpha():
        return False
    if text.endswith("_"):
        return False
    # 3) only letters, numbers and underscore
    if not re.fullmatch(r"[A-Za-z0-9_]+", text):
        return False
    return True


argument = input() if __name__ == "__main__" else ""
print(codeland_username_validation(argument))
