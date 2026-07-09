import json


def find_missing_number(numbers):
    # TODO: implement to find the single missing number in range 1..n
    real_cantidad = len(numbers) + 1
    presentes = [False] * (real_cantidad + 1)

    for numero in numbers:
        presentes[numero] = True

    for candidate in range(1, real_cantidad + 1):
        if not presentes[candidate]:
            return candidate

    return -1


try:
    raw = input()
    numbers = json.loads(raw) if raw else []
except Exception:
    numbers = []

print(find_missing_number(numbers))
