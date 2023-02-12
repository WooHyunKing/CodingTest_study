from collections import deque

n,m = map(int,input().split())

maze = []

visited = [[False]*m for _ in range(n)]

for _ in range(n):
    maze.append(list(map(int,input())))

def bfs(x,y):

    visited[x][y] = True
    
    queue = deque([(x,y)])

    while queue:
        v = queue.popleft()

        vx = v[0]
        vy = v[1]
        
        nx = [-1,1,0,0]
        ny = [0,0,-1,1]

        for i in range(4):

            temp_x = vx + nx[i]
            temp_y = vy + ny[i]
            
            if temp_x >= 0 and temp_x<n and temp_y >= 0 and temp_y <m:

                if (visited[temp_x][temp_y] == False) and (maze[temp_x][temp_y] != 0) :

                    queue.append((temp_x,temp_y))
                    visited[temp_x][temp_y] = True

                    maze[temp_x][temp_y] = maze[vx][vy] + 1

bfs(0,0)
print(maze[n-1][m-1])