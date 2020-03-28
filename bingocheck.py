import numpy as np
import arcade

board_1 = np.array(([13,16,39,52,61], [4,23,38,56,72], [12,22,45,60,62], [6, 21, 40, 59, 69],  [5,24,34,51,63]))
board_2 = np.array(([14,28,44,53,63], [12,16,36,57,72], [8,29,40,49,75], [10, 30, 43, 58, 62],  [7,20,45,54,67]))
test_list = np.array(([0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]))
test_board_two = np.array([test_list, board_1, board_2, board_1, board_1, board_1, board_1, board_1, board_1, board_2, board_2, board_2])


def check_board(board, correct_list):
    ver_len = len(board)
    hor_len = len(board[0])

    for i in range(ver_len):
        if check_list(board[i], correct_list) >= ver_len:
            print("BINGO!!!")
    
    for j in range(hor_len):
        if check_list(board[:,j], correct_list) >= hor_len:
            print("BINGO")


def check_list(list, correct):
    nb_correct = 0
    nb_correct = len(set(list).intersection(correct))
    return nb_correct


def print_board(board):
    for x in board:
        for y in x:
            print('\t', y, end='')
        print()

def main():
    print_board(board_1)
    print()
    print_board(board_2)
    check_board(board_1, test_list)


if __name__ == "__main__":
    main()