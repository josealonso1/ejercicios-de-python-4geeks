import json


def two_sum(nums, target):
    # TODO: implement and return the indices list
    return None


payload = {"nums": [], "target": 0}
try:
    raw = input()
    if raw:
        payload = json.loads(raw)
except Exception:
    payload = payload

result = two_sum(payload.get("nums", []), payload.get("target", 0))
print(result)
