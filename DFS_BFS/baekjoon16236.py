from collections import deque

n = int(input())

area = []
result = 0

shark_size = 2
ate_fish = 0

nx = [-1,1,0,0]
ny = [0,0,-1,1]

for i in range(n):
    area.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if area[i][j] == 9:
            shark_location_x, shark_location_y = i, j


def bfs(x,y,sharkSize):
    visited = [[False]*n for _ in range(n)]
    distence = [[0]*n for _ in range(n)]

    visited[x][y] = True

    queue = deque([(x,y)])

    temp = []
    
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다. (bfs사용)
    while queue:
        prev_x, prev_y = queue.popleft()

        for i in range(4):
            next_x = prev_x + nx[i]
            next_y = prev_y + ny[i]

            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                if area[next_x][next_y] <= sharkSize:
                    visited[next_x][next_y] = True
                    distence[next_x][next_y] = distence[prev_x][prev_y] + 1
                    queue.append((next_x,next_y))
                    if area[next_x][next_y] < sharkSize and area[next_x][next_y] != 0:
                        temp.append((next_x,next_y,distence[next_x][next_y]))

    return sorted(temp,key=lambda x:(-x[2],-x[0],-x[1]))

while True:

    location_list = bfs(shark_location_x,shark_location_y,shark_size)

    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if len(location_list) == 0:
        break
    
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    # 정렬한 결과를 반영해준다.
    x, y, dis = location_list.pop()

    #움직이는 칸수가 곧 시간이 된다.
    result += dis
    area[shark_location_x][shark_location_y], area[x][y]  = 0, 0
    
    #상어좌표를 먹은 물고기 좌표로 옮겨준다.
    shark_location_x, shark_location_y = x, y

    ate_fish += 1

    if ate_fish == shark_size:
        shark_size += 1
        ate_fish = 0
    

print(result)

    