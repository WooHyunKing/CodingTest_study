from collections import deque

n = int(input())

# 영역(2차원 리스트)
area = []

# 적록색약이 아닌 사람의 구역의 수
count_a = 0
# 적록색약인 사람의 구역의 수
count_b = 0

for _ in range(n):
    area.append(list(input()))

# 적록색약 X 방문 여부 2차원 리스트
visited_a = [[False]*n for _ in range(n)]
# 적록색약 O 방문 여부 2차원 리스트
visited_b = [[False]*n for _ in range(n)]

# 적록색약 X BFS함수
def bfs_a(x,y):
    
    if visited_a[x][y]:
        return False
    
    visited_a[x][y] = True
    
    queue = deque([(x,y)])
    
    while queue:
        v = queue.popleft()

        color = area[v[0]][v[1]]
        
        nx = [-1,1,0,0]
        ny = [0,0,-1,1]

        for i in range(4):
            temp_x = v[0] + nx[i]
            temp_y = v[1] + ny[i]
            
            if temp_x >=0 and temp_x < n and temp_y >=0 and temp_y < n and not visited_a[temp_x][temp_y]:
                if color == area[temp_x][temp_y]:
                    queue.append((temp_x,temp_y))
                    visited_a[temp_x][temp_y] = True
                
    
    return True

# 적록색약 O BFS함수
def bfs_b(x,y):
    
    if visited_b[x][y]:
        return False
    
    visited_b[x][y] = True
    
    queue = deque([(x,y)])
    
    while queue:
        v = queue.popleft()

        color = area[v[0]][v[1]]
        
        nx = [-1,1,0,0]
        ny = [0,0,-1,1]

        for i in range(4):
            temp_x = v[0] + nx[i]
            temp_y = v[1] + ny[i]
            
            if temp_x >=0 and temp_x < n and temp_y >=0 and temp_y < n and not visited_b[temp_x][temp_y]:
                if (color=='G' and area[temp_x][temp_y]=='R') or (color == 'R' and area[temp_x][temp_y] == 'G') or color == area[temp_x][temp_y] :
                    queue.append((temp_x,temp_y))
                    visited_b[temp_x][temp_y] = True
    
    return True

for i in range(n):
    for j in range(n):
        if bfs_a(i,j):
            count_a += 1

for i in range(n):
    for j in range(n):
        if bfs_b(i,j):
            count_b += 1


print(count_a,count_b)