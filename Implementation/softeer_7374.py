import sys

input = sys.stdin.readline

# 남우 부모님의 농사일을 도우려고 함

# 남우에게 할당된 땅은 3x3 크기의 격자
# 1 <= 각 땅의 높이 <= 3

# 부모님이 농사지을 땅의 크기는 1x3
# 농사를 짓기 위해서는 해당 영역 내 땅의 높이가 전부 동일해야 함 !!!

# 따라서 특정 땅의 높이를 낮추거나 높여서 3x3 격자 내에 부모님이 농사지을 수
# 있는 영역이 최소 1군데 이상 생기도록 만들려고 함

# 남우가 특정 땅의 높이를 1만큼 낮추거나 높이는데 1만큼의 비용이 소요

# 부모님께서 농사를 지으실 수 있도록 땅을 일구기 위해 남우에게 필요한 최소비용

area = [list(map(int,input().split())) for _ in range(3)]

available = False

answer = float("inf")

def check_row(n):

    value = area[n][0]

    for i in range(1,3):
        if value != area[n][i]:
            return False

    return True

def check_col(n):

    value = area[0][n]

    for i in range(1,3):
        if value != area[i][n]:
            return False

    return True

for i in range(3):
    if check_row(i):
        available = True
    if check_col(i):
        available = True

def calculate_row(n):

    global answer

    row_set = set(area[n])

    if len(row_set) == 2:
        answer = min(answer, max(row_set) - min(row_set))
    else:
        mok = sum(row_set) // 3
        temp = sum([abs(x-mok) for x in row_set])
        answer = min(answer, temp)

def calculate_col(n):

    global answer

    col_set = set([area[x][n] for x in range(3)])

    if len(col_set) == 2:
        answer = min(answer, (max(col_set) - min(col_set)) )
    else:
        mok = sum(col_set) // 3
        temp = sum([abs(x-mok) for x in col_set])
        answer = min(answer, temp)

if available:
    print(0)
else:
    for i in range(3):
        calculate_row(i)
        calculate_col(i)
    print(answer)