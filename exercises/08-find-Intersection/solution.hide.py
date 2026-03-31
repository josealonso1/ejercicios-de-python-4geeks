import json


def find_intersection(values):
    if not isinstance(values, list) or len(values) < 2:
        return False
    left = values[0].split(", ")
    right = values[1].split(", ")
    intersection = [item for item in left if item in right]
    return ",".join(intersection) if intersection else False


try:
    raw = input()
    values = json.loads(raw) if raw else []
except Exception:
    values = []

print(find_intersection(values))
