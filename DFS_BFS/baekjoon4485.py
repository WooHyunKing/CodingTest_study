# 젤다의 전설 게임에서 화폐의 단위는 루피(rupee)
# '도둑루피'라 불리는 검정색 루피도 존재하는데, 이걸 획득하면 오히려 소지한 루피가 감소하게 된다

# 링크는 지금 도둑루피만 가득한 N x N 크기의 동굴의 제일 왼쪽 위에 있다
# 링크는 이 동굴의 반대편 출구, 제일 오른쪽 아래 칸인 [N-1][N-1]까지 이동해야 한다

# 동굴의 각 칸마다 도둑루피가 있는데, 이 칸을 지나면 해당 도둑루피의 크기만큼 소지금을 잃게 된다

# 링크가 잃을 수밖에 없는 최소 금액은 얼마일까?

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

INF = float("inf")

index = 0

while True:
    n = int(input())

    index += 1

    if n == 0:
        break

    def bfs():
        area = [list(map(int,input().split())) for _ in range(n)]
        visited = [[INF]*n for _ in range(n)]

        visited[0][0] = area[0][0]

        queue = deque([(0,0)])

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if not (0 <= nx < n and 0 <= ny < n):
                    continue

                if visited[nx][ny] == INF:
                    visited[nx][ny] = visited[x][y] + area[nx][ny]
                    queue.append((nx,ny))
                
                else:
                    if visited[x][y] + area[nx][ny] < visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + area[nx][ny]
                        queue.append((nx,ny))
        
        return visited[n-1][n-1]
    
    print(f"Problem {index}: {bfs()}")


    # queue = deque([(0,0,area[0][0])])

    # while queue:
    #     x, y, lose = queue.popleft()
    #     visited[x][y] = True        

    #     if x == n - 1 and y == n-1 and lose < answer:
    #         answer = lose

    #     for i in range(4):
    #         nx, ny = x + dx[i], y + dy[i]

    #         if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
    #             queue.append((nx,ny,lose+area[nx][ny]))

    # print(f"Problem {index}: {answer}")


    # queue = deque([(0,0)])

    
    


    # def dfs(x,y,lose):

    #     global answer

    #     # if lose >= answer:
    #     #     return
                            
    #     if x == n-1 and y == n-1:
    #         answer = lose
    #         return
        
    #     visited[x][y] = True

    #     for i in range(4):
    #         nx, ny = x + dx[i], y + dy[i]
            
    #         if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and lose+area[nx][ny] < answer:
    #             dfs(nx,ny,lose+area[nx][ny])

    #     visited[x][y] = False

    #     return
    
    # dfs(0,0,area[0][0])


        




    