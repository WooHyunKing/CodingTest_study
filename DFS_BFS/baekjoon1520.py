import sys
sys.setrecursionlimit(50000000);

m, n = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
nx, ny = [-1,1,0,0], [0,0,-1,1]

def dfs(x,y):
    
    # 도착 지점에 도달하면 1 리턴
    if x == (m-1) and y == (n-1):
        return 1
    # 이미 방문한 길이라면 경우의 수를 구하지 않고 해당 위치에서 출발하는 경우의 수 리턴
    if dp[x][y] != -1:
        return dp[x][y]
    
    way_count = 0

    for i in range(4):
        temp_x = x + nx[i]
        temp_y = y + ny[i]

        if temp_x >= 0 and temp_x < m and temp_y >= 0 and temp_y < n and area[temp_x][temp_y] < area[x][y]:
                way_count += dfs(temp_x,temp_y)
    
    dp[x][y] = way_count

    return dp[x][y]

print(dfs(0,0))