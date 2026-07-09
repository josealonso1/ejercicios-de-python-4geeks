import json


def find_intersection(values):
    # TODO: implement intersection logic
    # `values` is expected to be a list with two strings like "1, 3, 4" and "1, 2, 4"
    if not isinstance(values, list) or len(values) < 2:
        return False
    primera = values[0].split(", ")
    segunda = values[1].split(", ")
    interseccion = [item for item in primera if item in segunda]
    resultado = ",".join(interseccion) if interseccion else False
    return resultado

try:
    raw = input()
    argument = json.loads(raw) if raw else []
except Exception:
    argument = []

print(find_intersection(argument))
