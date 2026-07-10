import json


def max_sub_array(nums):
    # TODO: implement Kadane's algorithm and return the max sum
    maximo_numero = nums[0]
    numero_actual = nums[0]

    for numero in nums[1:]:
        numero_actual = max(numero, numero_actual + numero)
        maximo_numero = max(numero_actual,maximo_numero)

    return maximo_numero


try:
    raw = input()
    nums = json.loads(raw) if raw else []
except Exception:
    nums = []

print(max_sub_array(nums))
