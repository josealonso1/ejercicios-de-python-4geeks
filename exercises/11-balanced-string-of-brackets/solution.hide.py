def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in text:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        elif char in pairs.values():
            stack.append(char)

    return len(stack) == 0


print(is_balanced(input()))
