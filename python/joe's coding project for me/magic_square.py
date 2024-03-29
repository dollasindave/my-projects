square = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

all_nums_array = []


def print_square():
    '''Prints the magic square'''
    for i in range(0, 3):
        for j in range(0, 3):
            print(square[i][j], end=" ")
        print()


def check_row():
    '''Checks to see if the row adds to 15'''
    row = False
    for i in range(0, 3):
        num = 15
        num -= int(square[i][0]) + int(square[i][1]) + int(square[i][2])
        if num == 0:
            row = True
        if num != 0:
            return False
    return row


def check_column():
    '''Checks to see if the column adds to 15'''
    col = False
    for i in range(0, 3):
        num = 15
        num -= int(square[0][i]) + int(square[1][i]) + int(square[2][i])
        if num == 0:
            col = True
        if num != 0:
            return False
    return col


def check_diag():
    '''Checks to see if the diagonal adds to 15'''
    diag = False
    num = 15
    num -= int(square[0][0]) + int(square[1][1]) + int(square[2][2])
    if num == 0:
        diag = True
    if num != 0:
        return False

    num = 15
    num -= int(square[2][0]) + int(square[1][1]) + int(square[0][2])
    if num == 0:
        diag = True
    if num != 0:
        return False
    return diag


def all_nums():
    '''Checks for all nums 1-9'''
    all_nums_array.append(int(square[0][0]))
    for i in range(0, 3):
        for j in range(0, 3):
            if not (i == 0 and j == 0):
                for element in all_nums_array:
                    if int(square[i][j]) == element:
                        return False
                all_nums_array.append(int(square[i][j]))
    return True


def main():
    '''Runs everything'''
    print("Your square is:")
    print_square()
    if check_row() and check_diag() and check_column() and all_nums():
        print("It is a Lo Shu magic square")
    else:
        print("Nope")


main()
