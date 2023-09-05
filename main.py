import random

br = [['', '', ''],
      ['', '', ''],
      ['', '', '']]


def print_fields(board, a, b, r=0):
    for i in range(a, b):
        p = i
        if board[r][i - a] != '':
            p = board[r][i - a]
        print(f"|   {p}   ", end="")
    print("|")


def display_board(board):
    print("+-------+-------+-------+",
          "|       |       |       |", sep="\n")
    print_fields(board, 1, 4, 0)
    print("|       |       |       |",
          "+-------+-------+-------+",
          "|       |       |       |", sep="\n")
    print_fields(board, 4, 7, 1)
    print("|       |       |       |",
          "+-------+-------+-------+",
          "|       |       |       |", sep="\n")
    print_fields(board, 7, 10, 2)
    print("|       |       |       |",
          "+-------+-------+-------+", sep="\n")


def enter_move(board):
    while True:
        r = int(input("Wykonaj swój ruch: "))
        if board[(r-1) // 3][r % 3 - 1] == '':
            board[(r-1) // 3][r % 3 - 1] = 'O'
            break
        print("Podałeś zajęte już pole, spróbuj ponownie")


def make_list_of_free_fields(board):
    f = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                f.append((i, j))
    return f


def victory_for(board, sign='X'):
    if ((board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or
            (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign)):
        print('ZWYCIESTWO', sign)
        return True
    for i in range(3):
        hpass = []
        vpass = []
        for j in range(3):
            if board[i][j] == sign:
                hpass.append(sign)
            if board[j][i] == sign:
                vpass.append(sign)
        if len(hpass) == 3 or len(vpass) == 3:
            print('ZWYCIESTWO', sign)
            return True
    return False


def draw_move(board):
    f = make_list_of_free_fields(board)
    if (1, 1) in f:
        board[1][1] = 'X'
    else:
        p = random.randrange(0, len(f))
        board[f[p][0]][f[p][1]] = 'X'


while True:
    draw_move(br)
    display_board(br)
    if victory_for(br):
        break
    enter_move(br)
    display_board(br)
    if victory_for(br, 'O'):
        break
