import re


def longest_word(sentence):
    longest = ""
    for raw_word in sentence.split():
        clean_word = re.sub(r"[^\w\s]", "", raw_word)
        if len(clean_word) > len(longest):
            longest = clean_word
    return longest


input_text = input("Write a sentence here\n")
print(longest_word(input_text))
