def letter_changes(text):
    # TODO: implement the algorithm described in the README.
    actualizacion = []
    simbolos = ["a","e","i","o","u"]

    for caracter in text:
        if not caracter.isalpha():
            actualizacion.append(caracter)
            continue
        
        if caracter == "z":
            next_caracter = "a"
        elif caracter == "Z":
            next_caracter = "A"
        else:
            next_caracter = chr(ord(caracter) + 1)

        if next_caracter.lower() in simbolos:
            next_caracter = next_caracter.upper()

        actualizacion.append(next_caracter)
    return "".join(actualizacion)


input_text = input("Write a sentence here\n")
print(letter_changes(input_text))
