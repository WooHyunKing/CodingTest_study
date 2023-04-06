from collections import deque

m,n,k = map(int,input().split())

area = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]

count_list = []

for i in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    
    for j in range(y1,y2):
        for k in range(x1,x2):
            area[j][k] = 1

def bfs(x,y):

    if visited[x][y] or area[x][y] == 1:
        return False
    
    count = 1
    
    queue = deque([(x,y)])
    visited[x][y] = True
    
    while queue:

        v = queue.popleft()
        
        nx = [-1,1,0,0]
        ny = [0,0,-1,1]
        
        for i in range(4):
            temp_x = v[0] + nx[i]
            temp_y = v[1] + ny[i]

            if temp_x >= 0 and temp_x < m and temp_y >=0 and temp_y < n:
                if area[temp_x][temp_y] == 0 and not visited[temp_x][temp_y]:
                    count += 1
                    visited[temp_x][temp_y] = True
                    queue.append((temp_x,temp_y))
        
    count_list.append(count)
    
    return True

for i in range(m):
    for j in range(n):
        bfs(i,j)

count_list.sort()

print(len(count_list))
for i in count_list:
    print(i,end=" ")