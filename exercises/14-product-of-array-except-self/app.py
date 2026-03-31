import json


def product_except_self(nums):
    # TODO: return a list where each index has the product of all other values
    return []


try:
    raw = input()
    nums = json.loads(raw) if raw else []
except Exception:
    nums = []

print(product_except_self(nums))
