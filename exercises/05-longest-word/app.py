import re


def longest_word(sentence):
    # TODO: return the longest word in `sentence`.
    # If there is a tie, return the first longest word.
    # Ignore punctuation.
    resultado = ""
    for palabra in sentence.split():
        palabra_limpia = re.sub(r"[^\w\s]", "", palabra)
        if palabra_limpia > resultado:
            resultado = palabra_limpia
    return resultado


input_text = input("Write a sentence here\n")
print(longest_word(input_text))
