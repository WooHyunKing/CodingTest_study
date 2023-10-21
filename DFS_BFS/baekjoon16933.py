from collections import deque

n, m, k = map(int,input().split())

visited =[[[0]*m for _ in range(n)] for _ in range(k+1)]

area = [list(map(int,list(input()))) for _ in range(n)]

queue = deque([(0,0,0,1)])

dx = [-1,1,0,0]
dy = [0,0,-1,1]


while queue:
    x,y,broken,ans = queue.popleft()

    if x == n-1 and y == m-1:
        print(ans)
        exit()
    
    daytime = ans % 2  # ans=1일 경우 낮 / ans=0 일 경우 밤, 
    # ans가 +1증가했다는 것은 낮에서 밤 또는 밤에서 낮으로 바뀐것을 의미

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if area[nx][ny] == 0 and visited[broken][nx][ny] == 0:
                visited[broken][nx][ny] = ans
                queue.append((nx,ny,broken,ans+1))
            if area[nx][ny] == 1 and broken < k and visited[broken+1][nx][ny] == 0:
                if daytime: # 낮인 경우
                    visited[broken+1][nx][ny] = ans
                    queue.append((nx,ny,broken+1,ans+1))
                else: # 밤인 경우
                    queue.append((x,y,broken,ans+1))

print(-1)
