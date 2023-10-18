# 8 <= n, m <= 50
n, m = map(int,input().split())

board = [list(input()) for _ in range(n)]

white_board = [['']*8 for _ in range(8)]
black_board = [['']*8 for _ in range(8)]

start_with_white = True

min_value = float("inf")

for i in range(8):
    for j in range(8):
        if start_with_white:
            white_board[i][j] = "W"
            black_board[i][j] = "B"
        else:
            white_board[i][j] = "B"
            black_board[i][j] = "W"
        if j != 7:
            start_with_white = not start_with_white

def calculate_diff_with_white(arr):
    diff = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] != white_board[i][j]:
                diff += 1
    
    return diff

def calculate_diff_with_black(arr):
    diff = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] != black_board[i][j]:
                diff += 1
    
    return diff

for i in range(n):
    for j in range(m):
        if (i + 7) < n and (j + 7) < m:
            temp_board = []
            for k in range(8):
                temp_board.append(board[i+k][j:j+8])
            min_value = min(calculate_diff_with_black(temp_board),calculate_diff_with_white(temp_board),min_value)

print(min_value)