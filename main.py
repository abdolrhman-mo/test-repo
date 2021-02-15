import pprint
import sys


def printBoard(board):
    print(f"{board['top-L']} | {board['top-M']} | {board['top-R']}")
    print('--+---+--')
    print(f"{board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print('--+---+--')
    print(f"{board['low-L']} | {board['low-M']} | {board['low-R']}")
    print()


def exit(myInput):
    if myInput == "":
        sys.exit()


topMidLow = ['low', 'mid', 'top']
xs = 'LMR'

board = {}

for y in topMidLow:
    for x in xs:
        board.setdefault(f"{y}-{x}", ' ')

# pprint.pprint(board)

# TODO include player names

# START GAME

print("Player 1 => X")
print("Player 2 => O")

# illustration
print()
print(f"top-L | top-M | top-R")
print('----- + ----- + -----')
print(f"mid-L | mid-M | mid-R")
print('----- + ----- + -----')
print(f"low-L | low-M | low-R")
print()

printBoard(board)

x_or_o = ["X", "O"]


def play(player_num):
    while True:
        print(f"player {player_num}: ", end="")
        play = input()

        exit(play)

        statement = False
        for position in board.keys():
            if position in play and board[position] == " ":
                # print(position)
                board[position] = x_or_o[int(player_num) - 1]
                statement = True
        if statement == False:
            print()
            print("Try again")
            print()
        else:
            break

    printBoard(board)


def check_win():
    # check if there is a match on x axics
    for y in topMidLow:
        if board[f'{y}-{xs[0]}'] == board[f'{y}-{xs[1]}'] == board[f'{y}-{xs[2]}'] != " ":
            if board[f'{y}-{xs[1]}'] != " ":
                if board[f'{y}-{xs[2]}'] != " ":
                    if board[f'{y}-{xs[0]}'] == "X":
                        print("player 1 wins")
                        print()
                        sys.exit()
                    elif board[f'{y}-{xs[0]}'] == "O":
                        print("player 2 wins")
                        print()
                        sys.exit()

    # check if there is a match on y axics
    for x in xs:
        if board[f"top-{x}"] == board[f"mid-{x}"] == board[f"top-{x}"] != " ":
            if board[f"mid-{x}"] != " ":
                if board[f"top-{x}"] != " ":
                    if board[f"top-{x}"] == "X":
                        print("player 1 wins")
                    else:
                        print("player 2 wins")

    # check if there is a cross match
    if board["top-L"] == board["mid-M"] == board["low-R"] != " ":
        if board["mid-M"] != " ":
            if board["low-R"]:
                if board["mid-M"] == "X":
                    print("player 1 wins")
                else:
                    print("player 2 wins")

    if board["top-R"] == board["mid-M"] == board["low-L"] != " ":
        if board["mid-M"] != " ":
            if board["low-L"] != " ":
                if board["mid-M"] == "X":
                    print("player 1 wins")
                else:
                    print("player 2 wins")


# TODO Play again?


while True:
    play("1")
    check_win()

    play("2")
    check_win()
