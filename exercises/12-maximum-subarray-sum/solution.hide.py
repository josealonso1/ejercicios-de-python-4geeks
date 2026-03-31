import json


def max_sub_array(nums):
    max_so_far = nums[0]
    current_max = nums[0]

    for number in nums[1:]:
        current_max = max(number, current_max + number)
        max_so_far = max(max_so_far, current_max)

    return max_so_far


try:
    raw = input()
    nums = json.loads(raw) if raw else []
except Exception:
    nums = []

print(max_sub_array(nums))
