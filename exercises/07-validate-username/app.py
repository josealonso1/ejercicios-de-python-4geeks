import re


def codeland_username_validation(text):
    # TODO: implement validation rules
    # 1) between 4 and 25 chars
    # 2) starts with a letter
    # 3) only letters, numbers and underscore
    # 4) does not end with underscore
    return False


argument = input() if __name__ == "__main__" else ""
print(codeland_username_validation(argument))
