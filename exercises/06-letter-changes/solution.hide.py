def letter_changes(text):
    updated = []
    vowels = {"a", "e", "i", "o", "u"}

    for char in text:
        if not char.isalpha():
            updated.append(char)
            continue

        if char == "z":
            next_char = "a"
        elif char == "Z":
            next_char = "A"
        else:
            next_char = chr(ord(char) + 1)

        if next_char.lower() in vowels:
            next_char = next_char.upper()

        updated.append(next_char)

    return "".join(updated)


input_text = input("Write a sentence here\n")
print(letter_changes(input_text))
