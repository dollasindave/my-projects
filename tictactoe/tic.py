print("This is tic tac toe")

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def print_board():
    """Print the current state of the board"""
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")


def is_available(row, col):
    """Checks to see if a space is available"""
    if board[row][col] == "-":
        return True
    else:
        return False


def take_turn(row, col, turn):
    """Takes a turn by putting an X or O in the selected space"""
    if is_available(row, col):
        if turn % 2 == 1:
            board[row][col] = "X"
        else:
            board[row][col] = "O"


def get_row():
    """Prompts the player for a row"""
    ro = None
    while True:
        player_row = input("Enter the row: ")
        if player_row.isdigit():
            ro = int(player_row)
        if ro < 0 or ro > 2:
            print("Print please enter a valid row: ")
        else:
            return ro


def get_col():
    """Prompts the player for a column"""
    co = None
    while True:
        player_column = input("Enter the column: ")
        if player_column.isdigit():
            co = int(player_column)
        if co < 0 or co > 2:
            print("Print please enter a valid column: ")
        else:
            return co


def check_win_row():
    """Checks for a win in each row"""
    for index, value in enumerate(board):
        if value == "X":
            if (value == board[index][1]) and board[index][1] == board[index][2]:
                return True, "X"
        elif value == "O":
            if (value == board[index][1]) and board[index][1] == board[index][2]:
                return True, "O"

    return False, None


def check_win_column():
    """Checks for a win in each column"""
    for i in range(0, 3):
        if board[0][i] == "X":
            if (board[0][i] == board[1][i]) and board[1][i] == board[2][i]:
                return True, "X"
        elif board[0][i] == "O":
            if (board[0][i] == board[1][i]) and board[1][i] == board[2][i]:
                return True, "O"

    return False, None


def check_win_diag():
    """Checks for a win in both diagonals"""
    if board[1][1] == "X":
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True, "X"
        elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            return True, "X"
    elif board[1][1] == "O":
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True, "O"
        elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            return True, "O"

    return False, None


def check_win():
    """Checks all ways to win to see if there is a win"""
    win_row, player_row = check_win_row()
    win_col, player_col = check_win_column()
    win_diag, player_diag = check_win_diag()

    if win_row:
        print_board()
        print(f"{player_row} wins!")
        return True
    elif win_col:
        print_board()
        print(f"{player_col} wins!")
        return True
    elif win_diag:
        print_board()
        print(f"{player_diag} wins!")
        return True

    # print_board()
    return False


def play_game():
    """Plays the game"""
    counter = 1
    player_turn = 1
    while counter < 10:
        print_board()
        while True:
            ro = get_row()
            co = get_col()
            if is_available(ro, co):
                take_turn(ro, co, player_turn)
                player_turn += 1
                counter += 1
                break
            else:
                print("Please enter a valid space")
        someone_won = check_win()
        if someone_won:
            break
    if not someone_won:
        print_board()
        print("It was a draw :(")
        print("Get better at the game")


play_game()
