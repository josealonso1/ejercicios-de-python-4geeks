import json


def reduce_gifts(prices=None, k=3, threshold=14):
    if prices is None:
        prices = []
    if k <= 0 or len(prices) < k:
        return 0

    values = list(prices)
    removed = 0

    while True:
        changed = False

        for index in range(len(values) - k + 1):
            window = values[index:index + k]
            if sum(window) > threshold:
                max_value = max(window)
                remove_at = index + window.index(max_value)
                values.pop(remove_at)
                removed += 1
                changed = True
                break

        if not changed or len(values) < k:
            break

    return removed


payload = {"prices": [3, 2, 1, 4, 6, 5], "k": 3, "threshold": 14}
try:
    raw = input()
    if raw:
        payload = json.loads(raw)
except Exception:
    payload = payload

print(reduce_gifts(payload.get("prices", []), payload.get("k", 0), payload.get("threshold", 0)))
