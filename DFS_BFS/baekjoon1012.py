# 테스트케이스 수
t = int(input())

count_list = []

def dfs(x,y):
    
    if area[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        
        nx = [-1,1,0,0]
        ny = [0,0,-1,1]
        
        for i in range(4):
            temp_x = x + nx[i]
            temp_y = y + ny[i]

            if temp_x >= 0 and temp_x < n and temp_y >=0 and temp_y < m:
                if area[temp_x][temp_y] == 1 and not visited[temp_x][temp_y]:
                    dfs(temp_x,temp_y)

        return True
    else:
        return False

for _ in range(t):
    # 세로(n), 가로(m), 배추 개수(k)
    m, n, k = map(int,input().split())

    area = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    count = 0

    for _ in range(k):
        y, x = map(int,input().split())
        area[x][y]=1

    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                count+=1

    count_list.append(count)


for i in count_list:
    print(i)