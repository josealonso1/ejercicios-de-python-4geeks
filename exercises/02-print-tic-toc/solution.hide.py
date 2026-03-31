for number in range(1, 101):
    if number % 15 == 0:
        print("TicToc")
    elif number % 3 == 0:
        print("Tic")
    elif number % 5 == 0:
        print("Toc")
    else:
        print(number)
