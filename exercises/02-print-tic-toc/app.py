# TODO: Write your solution here.
# Print numbers from 1 to 100.
# Multiples of 3 => "Tic", multiples of 5 => "Toc", multiples of both => "TicToc".
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("TicToc")
    elif num % 3 == 0:
        print("Tic")
    elif num % 5 == 0:
        print("toc")
    else:
        print(num)
