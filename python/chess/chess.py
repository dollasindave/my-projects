# this is gonna be sick
# i love this game

print("Let's play chess!")
print()

# put periods to determine color
# thanks joe
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


def print_board():
    '''This method prints the board'''
    for _, value in enumerate(board):
        for _, piece in enumerate(value):
            print(piece, end=" ")
        print()


def get_move():
    '''This method prompts the user for a move'''
    move = input("Enter a move: ")
    return move


def check_move(this_player):
    '''Checks if a move is valid'''
    # finds out which player's turn it is
    move = get_move()
    if this_player % 2 == 0:
        player = "white"
    else:
        player = "black"

    piece = move[:1]

    # piece is pawn
    if piece == "a" or piece == "b" or piece == "c" or piece == "d" or piece == "e" or piece == "f" or piece == "g" or piece == "h":
        has_extra = False
        takes = "x" in move
        reverse = move[::-1]
        if reverse[:1] == "+" or reverse[:1] == "#" or "=" in reverse:
            has_extra = True
        if not has_extra and not takes:
            file = piece
            column = ord(file) - 97
            row = int(move[1:2])
            print(column)

        if player == "white":
            is_in_row = False
            for i in range(row, 0, -1):
                square = board[i][column]
                piece_on_square = square.strip()
                if piece_on_square == "P":
                    piece_row = i
                    piece_column = column
                    is_in_row = True
                    break

            if not is_in_row:
                return False, move
            difference = row - piece_row + 1
            if not (difference <= 2 and piece_row == 2):
                return False, move

            square_contains = move.strip()
            if square_contains == "-":
                return True, move

    # use .strip() to get the contents of squares
    return False, move


def make_move(make_this_move, for_this_player):
    '''Makes the selected move'''
    move = make_this_move
    piece = make_this_move[:1]
    move.replace(piece, "")
    print(f"Remaining move {move}")


def main():
    '''Runs the whole thing'''
    print_board()
    play_game = True
    player = 0
    while play_game:
        is_legal = False
        while not is_legal:
            is_legal, move = check_move(player)
        make_move(move, player)
        print_board()
        if player % 2 == 0:
            print(f"White's move was {move}")
            print("Black's turn!")
        elif player % 2 == 1:
            print(f"Black's move was {move}")
            print("White's turn!")
        player += 1


main()
