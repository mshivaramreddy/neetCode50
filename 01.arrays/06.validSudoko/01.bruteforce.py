from typing import List
def validSudoko(board: List[List]) -> bool:
    for row in range(9):
        seen = set()
        for i in range(9):
            if board[row][i] == '.':
                continue
            if board[row][i] in seen:
                return False
            seen.add(board[row][i])

    for column in range(9):
        seen = set()
        for i in range(9):
            if board[i][column] == '.':
                continue
            if board[i][column] in seen:
                return False
            seen.add(board[column][i])

    for square in range(9):
        seen = set()
        for i in range(3):
            for j in range(3):
                row = (square // 3) * 3 + i
                col = (square % 3) * 3 + j
                print(board[row][col])
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
    return False

        





board = [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","8",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]]

result = validSudoko(board)
print(result)