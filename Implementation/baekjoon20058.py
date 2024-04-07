import copy
from collections import deque

n, q = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(2**n)]

visited = [[False]*len(area) for _ in range(len(area))]

l_list = list(map(int,input().split()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

total = 0
maximum = 0

def rotate90(i,j, area, n, new_area): # 오른쪽으로 90도 회전해서 저장하는 함수

    for r in range(n):
        for c in range(n):
            new_area[i+c][j+n-1-r] = area[i+r][j+c]
    

def fire(n): # 단계 L에 따라 회전시킨 후 얼음을 녹이는 함수

    global area
    
    malt_list = []
    new_area = [[0]*len(area) for _ in range(len(area))]

    for i in range(0,len(area),2**n):
        if i >= len(area):
            break
        for j in range(0,len(area),2**n):
            if j >= len(area):
                break
            rotate90(i,j,area,2**n,new_area)
    
    area = new_area

    for i in range(len(area)):
        for j in range(len(area)):

            ice_count = 0

            if area[i][j] == 0:
                continue

            for k in range(4):
                temp_x, temp_y = i+dx[k], j + dy[k]
                if 0 <= temp_x < len(area) and 0 <= temp_y < len(area) and area[temp_x][temp_y] > 0:
                    ice_count += 1
            
            if ice_count < 3 and area[i][j] > 0:
                malt_list.append((i,j))

    for x, y in malt_list:
        area[x][y] -= 1

def bfs(x,y): # (x,y) 좌표에 연결된 얼음 덩어리 면적을 반환하는 함수
    
    if area[x][y] == 0 or visited[x][y]:
        return -1
    
    count = 0
    
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        current_x, current_y = queue.popleft()

        count += 1

        for i in range(4):
            next_x, next_y = current_x+dx[i], current_y+dy[i]

            if 0 <= next_x < len(area) and 0 <= next_y < len(area) and area[next_x][next_y] > 0 and not visited[next_x][next_y]:
                queue.append((next_x,next_y))
                visited[next_x][next_y] = True

    return count

for l in l_list:
    fire(l)

for i in range(len(area)):
    for j in range(len(area)):
        total += area[i][j]
        temp_count = bfs(i,j)

        if temp_count > maximum:
            maximum = temp_count

for i in area:
    print(i)

print(total)
print(maximum)