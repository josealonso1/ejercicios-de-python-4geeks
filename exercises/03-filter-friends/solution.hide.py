import json


def friend(friends):
    if not isinstance(friends, list):
        return []
    return [name for name in friends if isinstance(name, str) and len(name) == 4]


try:
    raw = input()
    values = json.loads(raw) if raw else []
except Exception:
    values = []

print(friend(values))
