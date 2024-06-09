# 판의 가장자리에는 치즈가 놓여 있지 않다.
# 치즈에는 하나 이상의 구멍이 있을 수 있다.
# 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다.
# 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다.

# 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r, c = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(r)]

melt_count_list = []

time = 0

def melt():
    
    queue = deque([(0,0)])

    melt_list = []

    while queue:
        
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if area[nx][ny] == 1:
                    melt_list.append((nx,ny))
                elif area[nx][ny] == 0:
                    queue.append((nx,ny))

                visited[nx][ny] = True

    for mx, my in melt_list:
        area[mx][my] = 0

    melt_count_list.append(len(melt_list))

    return len(melt_list)
    
while True:
    
    visited = [[False]*c for _ in range(r)]

    count = melt()

    if count == 0:
        print(time)
        print(melt_count_list[-2])
        break

    time += 1
    

    


# melt_counts = []

# time = 0

# def bfs():
    
#     queue = deque()
#     queue.append((0,0))
#     visited[0][0] = True

#     count = 0
    
#     while queue:

#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
#                 if area[nx][ny] == 0:
#                     queue.append((nx,ny))
#                 if area[nx][ny] == 1:
#                     area[nx][ny] = 0
#                     count += 1
#                 visited[nx][ny] = True
#     melt_counts.append(count)

#     return count

# while True:
#     visited = [[False]*c for _ in range(r)]

#     melt_count = bfs()
    
#     if melt_count == 0:
#         print(time)
#         print(melt_counts[-2])
#         break

#     time += 1