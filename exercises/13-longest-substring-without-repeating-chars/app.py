def length_of_longest_substring(text):
    # TODO: implement the sliding window solution returning the length
    conjunto_letras = set()
    izq = 0
    conteo_maximo = 0

    for der in range(len(text)):
        while text[der] in conjunto_letras:
            conjunto_letras.remove(text[izq])
            izq += 1 

        conjunto_letras.add(text[der])

        conteo_maximo = max(conteo_maximo, der - izq + 1)

    return conteo_maximo


argument = input() if __name__ == "__main__" else ""
print(length_of_longest_substring(argument))
