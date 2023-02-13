from collections import deque

n,m = map(int,input().split())

# n x m 크기의 미로
maze = []

# 방문 여부 확인용 2차원 배열
visited = [[False]*m for _ in range(n)]

# 미로 입력받고 저장
for _ in range(n):
    maze.append(list(map(int,input())))

# bfs 함수
def bfs(x,y):

    # 방문 처리
    visited[x][y] = True
    
    # queue 자료구조 선언
    queue = deque([(x,y)])

    while queue:
        v = queue.popleft()

        vx = v[0]
        vy = v[1]
        
        nx = [-1,1,0,0]
        ny = [0,0,-1,1]

        # 상-하-좌-우 탐색
        for i in range(4):

            temp_x = vx + nx[i]
            temp_y = vy + ny[i]
            
            # 배열의 범위를 벗어나는지 확인
            if temp_x >= 0 and temp_x<n and temp_y >= 0 and temp_y <m:

                # 방문했는지 여부 / 이동가능한 칸인지 확인
                if (visited[temp_x][temp_y] == False) and (maze[temp_x][temp_y] != 0) :
                    # 이동 가능하다면 큐에 추가
                    queue.append((temp_x,temp_y))
                    # 방문처리
                    visited[temp_x][temp_y] = True
                    # 한칸 씩 이동할 때마다 이전 값 +1 처리
                    maze[temp_x][temp_y] = maze[vx][vy] + 1

bfs(0,0) # (0,0)부터 시작
print(maze[n-1][m-1]) # 최종 (n,m)값(최소 칸수)