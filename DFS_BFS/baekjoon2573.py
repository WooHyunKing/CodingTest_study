from collections import deque
import copy
# 각 칸의 높이는 자연수로 저장
# 빙산이 아닌 바다는 0으로 저장

# 매년 동서남북에 존재하는 바다의 개수만큼 줄어듦
# 단, 각 칸의 저장된 높이는 0에서 더 줄어들지 X

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]

# 덩어리를 세는 함수(모든 칸을 BFS로 체크)
def count_area():
    count = 0
    visited = [[False]*m for _ in range(n)]
    
    # 빙산을 체크하는 BFS
    def bfs(x,y):

        if visited[x][y] or area[x][y] == 0:
            return False
    
        visited[x][y] = True
        queue = deque([(x,y)])

        while queue:
            cur_x, cur_y = queue.popleft()
        
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and area[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
        return True
    
    for i in range(1,n):
        for j in range(1,m):
            if count >= 2:
                return count
            if bfs(i,j):
                count += 1
    
    return count

# 빙산이 전부 다 녹았는지 확인하는 함수
def check_all_malt():
    for i in range(n):
        for j in range(m):
            if area[i][j] != 0:
                return False
    return True

# 상하좌우에 존재하는 바다의 개수를 구하는 함수
def count_sea(x,y,area):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 0:
            count += 1
    return count

# 1년 뒤 녹은 빙산을 반환하는 함수
def after_one_year():
    global area
    temp_area = copy.deepcopy(area)

    for i in range(1,n):
        for j in range(1,m):
            if area[i][j] != 0:
                temp_area[i][j] = max(0,area[i][j]-count_sea(i,j,area))

    area = temp_area

answer = 0

while True:
    answer += 1
    after_one_year()

    if count_area() >= 2:
        break

    if check_all_malt():
        answer = 0
        break

print(answer)