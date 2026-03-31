import json


def product_except_self(nums):
    length = len(nums)
    answer = [1] * length

    prefix = 1
    for index in range(length):
        answer[index] = prefix
        prefix *= nums[index]

    postfix = 1
    for index in range(length - 1, -1, -1):
        answer[index] *= postfix
        postfix *= nums[index]

    return answer


try:
    raw = input()
    nums = json.loads(raw) if raw else []
except Exception:
    nums = []

print(product_except_self(nums))
