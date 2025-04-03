from typing import List

problem = [
    [9, 0, 0, 0, 8, 0, 0, 0, 1],
    [0, 0, 0, 4, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 7, 0, 3, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [4, 0, 1, 0, 6, 0, 5, 0, 8],
    [0, 9, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 7, 0, 3, 0, 2, 0, 0],
    [0, 0, 0, 7, 0, 5, 0, 0, 0],
    [1, 0, 0, 0, 4, 0, 0, 0, 7]
]


solution = [
    [9, 2, 6, 5, 8, 3, 4, 7, 1],
    [7, 1, 3, 4, 2, 6, 9, 8, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 7, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [6, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7]
]


def num_in_column(board, indice_column) -> bool:
    possibles_nums = [c for c in range(1, 10)]
    for i in board:
        if i[indice_column] != 0:
            possibles_nums.remove(i[indice_column])
    return possibles_nums


def num_in_row(board, indice_row):
    possibles_nums = [c for c in range(1, 10)]
    nums_in_row = board[indice_row]
    for item in nums_in_row:
        if item != 0:
            possibles_nums.remove(item)
    return possibles_nums

def insert_num(board, row, column):
    possible_nums = set(num_in_column(board, column)) or set(num_in_row(board, row))   
    return list(possible_nums)

def solve(board) -> List[List[int]]:
    r, c = 0, 0
    while True:
        try:
            for row, i in enumerate(board):
                for column, j in enumerate(i):
                    if j == 0:
                        r, c = row, column
                        break
                if j == 0:
                    break        
            board[r][c] = insert_num(board, row, column)[0]
        except IndexError:
            break

    return board


if __name__ == "__main__":
    board = solve(problem)
    print(board)