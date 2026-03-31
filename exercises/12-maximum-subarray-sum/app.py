import json


def max_sub_array(nums):
    # TODO: implement Kadane's algorithm and return the max sum
    return 0


try:
    raw = input()
    nums = json.loads(raw) if raw else []
except Exception:
    nums = []

print(max_sub_array(nums))
