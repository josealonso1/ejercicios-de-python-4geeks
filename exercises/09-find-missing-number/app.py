import json


def find_missing_number(numbers):
    # TODO: implement to find the single missing number in range 1..n
    return -1


try:
    raw = input()
    numbers = json.loads(raw) if raw else []
except Exception:
    numbers = []

print(find_missing_number(numbers))
