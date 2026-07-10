import json


def product_except_self(nums):
    # TODO: return a list where each index has the product of all other values
    el_rango = len(nums)
    answer = [1] * el_rango

    recorrido_derecha = 1
    for n in range(el_rango):
        answer[n] = recorrido_derecha
        recorrido_derecha *= nums[n]

    recorrido_izquierda = 1
    for n in range(el_rango-1,-1,-1):
        answer[n] *= recorrido_izquierda
        recorrido_izquierda *= nums[n]

    return answer


try:
    raw = input()
    nums = json.loads(raw) if raw else []
except Exception:
    nums = []

print(product_except_self(nums))
