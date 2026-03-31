import json


def two_sum(nums, target):
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    return None


payload = {"nums": [], "target": 0}
try:
    raw = input()
    if raw:
        payload = json.loads(raw)
except Exception:
    payload = payload

print(two_sum(payload.get("nums", []), payload.get("target", 0)))
