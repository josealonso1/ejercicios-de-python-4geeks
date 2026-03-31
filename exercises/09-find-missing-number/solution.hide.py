import json


def find_missing_number(numbers):
    full_length = len(numbers) + 1
    present = [False] * (full_length + 1)

    for number in numbers:
        present[number] = True

    for candidate in range(1, full_length + 1):
        if not present[candidate]:
            return candidate

    return -1


try:
    raw = input()
    values = json.loads(raw) if raw else []
except Exception:
    values = []

print(find_missing_number(values))
