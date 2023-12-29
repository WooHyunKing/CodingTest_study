# 상근이는 불이 옮겨진 칸과 불이 붙으려는 칸으로 이동 X
# 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

# 빌딩의 지도가 주어졌을때, 얼마나 빨리 빌딩을 탈출할 수 있는가(최단 시간)

# 빌딩을 탈출하는 최단 시간, 불가능하다면 IMPOSSIBLE 출력

from collections import deque

t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(t):
    w, h = map(int,input().split())

    # 빈공간(.), 벽(#), 시작위치(@), 불(*)
    area = [list(input()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    
    fire_list = []

    enable_set = set()

    def addEnable(x,y): # 불이 붙으려는 칸을 이동 불가능한 집합에 추가하는 함수
        for i in range(4):
            temp_x, temp_y = x + dx[i], y + dy[i]
            if 0 <= temp_x < h and 0 <= temp_y < w and area[temp_x][temp_y] == '.':
                enable_set.add((temp_x,temp_y))

    for i in range(h):
        for j in range(w):
            if area[i][j] == "@":
                start_x, start_y = i, j
            
            if area[i][j] == "*":
                fire_list.append((i,j))
                addEnable(i,j)

    def bfs():
    
        queue = deque([(start_x,start_y,'sang')] + [(x,y,"fire") for x,y in fire_list])

        while queue:
            
            x, y, value = queue.popleft()

            for i in range(4):
                temp_x = x + dx[i]
                temp_y = y + dy[i]

                if 0 <= temp_x < h and 0 <= temp_y < w:
                    if value == "sang":
                        if area[temp_x][temp_y] == '.' and visited[temp_x][temp_y] == 0  and (temp_x,temp_y) not in enable_set:
                            queue.append((temp_x,temp_y,'sang'))
                            visited[temp_x][temp_y] = visited[x][y] + 1
                    elif value == "fire":
                        if area[temp_x][temp_y] == '.':
                            queue.append((temp_x,temp_y,'fire'))
                            area[temp_x][temp_y] = "*"
                            addEnable(temp_x,temp_y)
                else:
                    if value == "sang":
                        print(visited[x][y]+1)
                        return
        
        print("IMPOSSIBLE")
        return
                
    bfs()