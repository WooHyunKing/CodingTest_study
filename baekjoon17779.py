import sys
from collections import deque

input = sys.stdin.readline

# 구역을 다섯 개의 선거구로 나눠야 하고, 각 구역은 다섯 선거구 중 하나에 포함되어야 한다.
# 선거구는 구역을 적어도 하나 포함해야 하고, 
# 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다. 

# 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다
# 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.

# 구역 (r, c)의 인구는 A[r][c]이고, 선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값
# 선거구를 나누는 방법 중에서, 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값

N = int(input())

area = [list(map(int,input().split())) for _ in range(N)]

total = 0

answer = float("inf")

for i in range(N):
    for j in range(N):
        total += area[i][j]

def calculate(row,col,d1,d2):

    global answer
    
    first, second, third, fourth = 0, 0, 0, 0

    col1 = col + 1
    for r in range(row+d1):
        if r >= row:
            col1 -= 1
        first += sum(area[r][:col1])
    
    col2 = col + 1
    for r in range(row+d2+1):
        if r > row:
            col2 += 1
        second += sum(area[r][col2:])

    col3 = col - d1
    for r in range(row+d1,N):
        third += sum(area[r][:col3])
        if r < row+d1+d2:
            col3 += 1
    
    col4 = col+d2
    for r in range(row+d2+1,N):
        fourth += sum(area[r][col4:])
        if r <= row+d1+d2:
            col4 -= 1

    five = total - first - second - third - fourth

    answer = min(answer, max(first,second,third,fourth,five)-min(first,second,third,fourth,five))


def check(r,c,d1,d2):
    if 0 <= r+d1+d2 < N and 0 <= c-d1 < N and 0 <= c+d2 < N:
        calculate(r,c,d1,d2)

for r in range(N-2):
    for c in range(1,N-1):
        for d1 in range(1,N-1):
            for d2 in range(1,N-1):
                check(r,c,d1,d2)

print(answer)