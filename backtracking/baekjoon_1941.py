from itertools import combinations
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

area = [list(input()) for _ in range(5)]

positions = []

for i in range(5):
    for j in range(5):
        positions.append((i,j))

combs = list(combinations(positions,7))

answer = 0

def checkValid(givenComb): # 주어진 7개의 조합이 4개 이상의 다솜파 학생이 존재하는지 판단하는 함수
    s_count = 0
    for x,y in givenComb:
        if area[x][y] == "S":
            s_count += 1
    if s_count >= 4:
        return True
    else:
        return False

def checkAdjacent(givenComb): # 주어진 7개의 조합이 인접해 있는지 판단하는 함수
    visited = [False]*7

    q = deque([givenComb[0]])
    
    visited[0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) in givenComb:
                next_index = givenComb.index((nx,ny))
                if not visited[next_index]:
                    q.append((nx,ny))
                    visited[next_index] = True
    if False in visited:
        return False
    else:
        return True
    
for comb in combs:
    if checkValid(comb):
        if checkAdjacent(comb):
            answer += 1

print(answer)