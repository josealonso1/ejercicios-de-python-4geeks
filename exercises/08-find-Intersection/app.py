import json


def find_intersection(values):
    # TODO: implement intersection logic
    # `values` is expected to be a list with two strings like "1, 3, 4" and "1, 2, 4"
    return False


try:
    raw = input()
    argument = json.loads(raw) if raw else []
except Exception:
    argument = []

print(find_intersection(argument))
