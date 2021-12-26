def drawboard(mat):
    print("-"*8)
    print("|" + mat[0][0], mat[0][1], mat[0][2], "|")
    print("|" + mat[1][0], mat[1][1], mat[1][2], "|")
    print("|" + mat[2][0], mat[2][1], mat[2][2], "|")
    print("-"*8)


def check_row(mat, row):
    return (mat[row][0] == mat[row][1] and mat[row][1] == mat[row][2] and mat[row][0] != " ")


def check_column(mat, col):
    return (mat[0][col] == mat[1][col] and mat[1][col] == mat[2][col] and mat[0][col] != " ")


def check_diagonals(mat):
    return (mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[0][0] != " ") or \
           (mat[2][0] == mat[1][1] and mat[1][1] == mat[0][2] and mat[2][0] != " ")


def check_winner(mat):
    for i in range(3):
        if check_row(mat, i):
            return True
        if check_column(mat, i):
            return True
    if check_diagonals(mat):
        return True
    return False


def is_mat_full(mat):
    for item in mat:
        if " " in item:
            return False
    return True


def play(mat):
    while True:
        row = input("Enter row number: ")
        while not row.isdigit() or int(row) < 1 or int(row) > 3:
            row = input("Enter row number between 1-3: ")
        row = int(row)
        col = input("Enter column number: ")
        while not col.isdigit() or int(col) < 1 or int(col) > 3:
            col = input("Enter column number between 1-3: ")
        col = int(col)
        if mat[row - 1][col - 1] != " ":
            print("Pick an empty box!")
        else:
            return (row - 1, col - 1)


def main():
    print("\n== Tic Tac Toe ==")
    mat = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    players = ["X", "O"]

    turn = 0
    while not is_mat_full(mat):
        drawboard(mat)
        if turn == 0:
            print("You play!")
            row, col = play(mat)
            mat[row][col] = players[turn]

        else:
            print("Computer plays!")
            row, col = play(mat)
            mat[row][col] = players[turn]

        if check_winner(mat):
            drawboard(mat)
            print("X won!" if turn == 0 else "0 won!")
            break
        turn = 1 - turn
    else:
        drawboard(mat)
        print("It's a tie!")


main()
