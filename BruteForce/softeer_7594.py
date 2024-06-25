import sys

from itertools import combinations

input = sys.stdin.readline

# 최대 4번 인접해 있는 두 나무를 묶을 예정
# 묶은 나무끼리는 서로 겹쳐서는 안됨
# 두 나무가 묶였을 때 얻을 수 있는 아름다움은 '두 나무의 키의 합'과 동일
# 묶인 쌍의 아름다움의 합을 최대로 만들려고 함

n = int(input())

heights = [list(map(int,input().split())) for _ in range(n)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

answer = float("-inf")

datas = []

for i in range(n):
    for j in range(n):
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                datas.append(((i,j),(nx,ny)))

if n == 2:
    cases = list(combinations(datas,2))
else:
    cases = list(combinations(datas,4))

for case in cases:

    coors = []
    sum = 0

    for twice in case:
        coors += [twice[0], twice[1]]
        sum += (heights[twice[0][0]][twice[0][1]] + heights[twice[1][0]][twice[1][1]])
        
    if len(coors) == len(set(coors)):
        answer = max(answer,sum)

print(answer)