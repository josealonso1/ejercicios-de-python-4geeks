import json


def two_sum(nums, target):
    # TODO: implement and return the indices list
    historial = {}

    for index, value in enumerate(nums):
        complemento = target - value
        if complemento in historial:
            return [historial[complemento], index]
        historial[value] = index

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
