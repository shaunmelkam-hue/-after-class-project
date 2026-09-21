def filter_squares(start, end):
    evens = []
    odds = []
    for num in range(start, end + 1):
        square = num ** 2

        if square % 2 == 0:
            evens.append(square)
        else:
            odds.append(square)

    print("Even squares:", evens)
    print("Odd squares:", odds)
filter_squares(1, 5)