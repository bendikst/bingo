import numpy as np
import arcade

board_1 = np.array(([13,16,39,52,61], [4,23,38,56,72], [12,22,45,60,62], [6, 21, 40, 59, 69],  [5,24,34,51,63]))
board_2 = np.array(([14,28,44,53,63], [12,16,36,57,72], [8,29,40,49,75], [10, 30, 43, 58, 62],  [7,20,45,54,67]))
test_list = np.array(([1,2,3,4,5], [2,0,0,0,0], [3,0,0,0,0], [4,0,0,0,0], [5,0,0,0,0]))
test_board_two = np.array([test_list, board_1, board_2, board_1, board_1, board_1, board_1, board_1, board_1, board_2, board_2, board_2])
test_board_one = np.array([test_list, test_list, test_list, test_list, test_list])



def check_board(board, correct_list):
    l_size = len(board[0])
    nb_bingos = 0
    for j in range(l_size):
        if check_list(board[j], correct_list) >= l_size:
            nb_bingos += 1
    return nb_bingos


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