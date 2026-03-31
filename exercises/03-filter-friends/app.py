import json


def friend(friends):
    # TODO: write your solution here
    # `friends` will be a list of strings, for example ["Ryan", "Kieran", "Mark", "Miguel"]
    # Return a new list containing only the names that have exactly 4 characters.
    return []


# IGNORE BELOW THIS LINE
input_data = ["Ryan", "Kieran", "Ana", "Mark", "Miguel", "Meg"]

try:
    raw = input()
    if raw:
        input_data = json.loads(raw)
except Exception:
    input_data = []

print(friend(input_data))
