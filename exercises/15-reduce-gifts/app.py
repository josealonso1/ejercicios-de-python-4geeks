import json


def reduce_gifts(prices=None, k=3, threshold=14):
    if len(prices) < k:
        return 0

    eliminados = 0

    caja_actual = prices[:k]
    suma_actual = sum(caja_actual)
    if suma_actual > threshold:
        mas_caro = max(caja_actual)
        caja_actual.remove(mas_caro)
        suma_actual -= mas_caro
        eliminados += 1
    
    for i in range(k, len(prices)):
        nuevo_precio = prices[i]
        caja_actual.append(nuevo_precio)
        suma_actual += nuevo_precio

        if len(caja_actual) > k:
            precio_viejo = caja_actual.pop(0)
            suma_actual -= precio_viejo

        if suma_actual > threshold:
            mas_caro = max(caja_actual)
            caja_actual.remove(mas_caro)
            suma_actual -= mas_caro

            eliminados += 1

    # TODO: implement the algorithm and return an integer (number of removals)
    return eliminados


payload = {"prices": [9, 6, 7, 2, 7, 2], "k": 3, "threshold": 14}
try:
    raw = input()
    if raw:
        payload = json.loads(raw)
except Exception:
    payload = payload

print(reduce_gifts(payload.get("prices", []), payload.get("k", 0), payload.get("threshold", 0)))
