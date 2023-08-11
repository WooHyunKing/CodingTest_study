from copy import deepcopy
from collections import deque
import sys

sys.setrecursionlimit(10**7)

graph = [list(map(int,input().split())) for _ in range(3)]

final_graph = [[1,2,3],[4,5,6],[7,8,0]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = {}

temp_graph = deepcopy(graph)

for i in range(3):
    for j in range(3):
        if graph[i][j] == 0:
            first_x, first_y = i, j

def changeToString(arr): # 퍼즐의 상태를 문자열로 바꿔주는 함수
    str_arr = []
    for i in range(3):
        for j in range(3):
            str_arr.append(str(arr[i][j]))
    return "".join(str_arr)

def bfs(): # BFS 함수
    
    visited[changeToString(graph)] = 0
    
    queue = deque([(first_x,first_y,graph,0)])

    while queue:
        v = queue.popleft()
        x, y, g, c = v[0], v[1], v[2], v[3] # x값, y값, 그래프 상태, 이동거리

        changed_g = changeToString(g) # 그래프 상태 문자열로 변환

        if changed_g == '123456780': # 그래프 상태가 최종 상태랑 동일할 경우 Return
            return visited[changed_g]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 3 and 0 <= ny < 3:
                temp_g = deepcopy(g)
                temp_g[x][y], temp_g[nx][ny] = temp_g[nx][ny], temp_g[x][y] # 값 변경
                changed_temp_g = changeToString(temp_g)
                if changed_temp_g not in visited: # 다음 좌표가 방문한 적이 없다면
                    visited[changed_temp_g] = c+1 # 사전 자료형에 저장
                    queue.append((nx,ny,temp_g,c+1)) # 큐에 삽입

    return -1 # 큐에 더 이상 데이터가 없다면, 즉 최종 상태에 도달할 수 없다면 -1 반환

print(bfs())