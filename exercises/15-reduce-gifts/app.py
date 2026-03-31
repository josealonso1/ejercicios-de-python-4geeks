import json


def reduce_gifts(prices=None, k=3, threshold=14):
    if prices is None:
        prices = []

    # TODO: implement the algorithm and return an integer (number of removals)
    return 0


payload = {"prices": [3, 2, 1, 4, 6, 5], "k": 3, "threshold": 14}
try:
    raw = input()
    if raw:
        payload = json.loads(raw)
except Exception:
    payload = payload

print(reduce_gifts(payload.get("prices", []), payload.get("k", 0), payload.get("threshold", 0)))
