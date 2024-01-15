from collections import deque

h, w = map(int,input().split())

dx = [1,0,0]
dy = [0,1,-1]

area = [[0]*w for _ in range(h)]
visited = [[False]*w for _ in range(h)]

answer = 0

heights = list(map(int,input().split()))

def check_available(x,y): # 빗물이 고일 수 있는 영역인지 체크하는 함수(양옆에 블록이 쌓여 있어야함)
    
    left_side = False
    right_side = False

    for i in range(y+1,w):
        if area[x][i] == 1:
            right_side = True
    for i in range(y-1,-1,-1):
        if area[x][i] == 1:
            left_side = True

    return left_side and right_side


def bfs(x,y): # 영역을 탐색 및 카운팅하는 함수

    global answer

    if visited[x][y]:
        return

    visited[x][y] = True
    answer += 1

    queue = deque([(x,y)])

    while queue:
        temp_x, temp_y = queue.popleft()

        for i in range(3):
            next_x = temp_x + dx[i]
            next_y = temp_y + dy[i]

            if 0 <= next_x < h and 0 <= next_y < w and area[next_x][next_y] == 0 and not visited[next_x][next_y]:
                queue.append((next_x,next_y))
                visited[next_x][next_y] = True
                answer += 1

for index,height in enumerate(heights): # 블록 쌓기
    for i in range(height):
        area[h-i-1][index] = 1

for i in range(h):
    for j in range(w):
        if area[i][j] == 0 and check_available(i,j): # 모든 좌표를 순회하면서 빗물이 고일 수 있다면 방문처리 및 영역 카운팅
            bfs(i,j)

print(answer)