board = [
    [" R.", " N.", " B.", " Q.", " K.", " B.", " N.", " R."],
    [" P.", " P.", " P.", " P.", " P.", " P.", " P.", " P."],
    [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
    [" P ", " P ", " P ", " P ", " P ", " P ", " P ", " P "],
    [" R ", " N ", " B ", " Q ", " K ", " B ", " N ", " R "]
]

white_pieces = [" R ", " N ", " B ", " Q ", " K ", " B ", " N ",
                " R ", " P ", " P ", " P ", " P ", " P ", " P ", " P ", " P "]
black_pieces = [" R.", " N.", " B.", " Q.", " K.", " B.", " N.",
                " R.", " P.", " P.", " P.", " P.", " P.", " P.", " P.", " P."]


def check_check():
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j].strip() == "K":
                row, col = i, j


def main():
    print("Running!")


main()
