import sys
from collections import deque

input = sys.stdin.readline

# 일부분은 검은 방이고 나머지는 모두 흰 방이다.

# 검은 방은 사면이 벽으로 싸여 있어 들어갈 수 없다.
# 서로 붙어 있는 두 개의 흰 방 사이에는 문이 있어서 지나다닐 수 있다. 

# 윗줄 맨 왼쪽 방은 시작방으로서 항상 흰 방
# 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방

# 검은 방 몇 개를 흰 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.

n = int(input())

area = [list(map(int,list(input().rstrip()))) for _ in range(n)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

visited = [[float("inf")]*n for _ in range(n)]

def bfs():

    q = deque([(0,0)])

    visited[0][0] = 0

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] == 1 and visited[nx][ny] > visited[x][y]:
                    visited[nx][ny] = visited[x][y]
                    q.append((nx,ny))
                elif area[nx][ny] == 0 and visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    
    print(visited[n-1][n-1])

bfs()
                    



# black_list = []

# for i in range(n):
#     for j in range(n):
#         if area[i][j] == 0:
#             black_list.append((i,j))

            

# def combinations(arr,k):
    
#     cases = []

#     def dfs(elements,index):
        
#         if len(elements) == k:
#             cases.append(elements)
#             return
        
#         for i in range(index+1,len(arr)):
#             dfs(elements + [arr[i]],i)
    
#     dfs([],-1)

#     return cases

# def bfs(t_area):

#     # t_area = [x[:] for x in area]

#     visited = [[False]*n for _ in range(n)]

#     q = deque([(0,0)])

#     visited[0][0] = True

#     while q:

#         x, y = q.popleft()

#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]

#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and t_area[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 q.append((nx,ny))
    
#     if visited[n-1][n-1] == True:
#         return True
#     else:
#         return False
    
# def get_coors(t_area):

#     visited = [[False]*n for _ in range(n)]

#     q = deque([(0,0)])

#     visited[0][0] = True

#     coor = []

#     while q:

#         x, y = q.popleft()

#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]

#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:

#                 if t_area[nx][ny] == 1:
#                     visited[nx][ny] = True
#                     q.append((nx,ny))
#                 else:
#                     visited[nx][ny] = True
#                     coor.append((nx,ny))
#     return coor

# print(get_coors(area))
    
# if bfs(area):
#     print(0)
#     exit()

# answer = 0

# while True:

#     temp_coors = get_coors(area) # [(2, 1), (1, 2), (0, 3), (4, 0), (5, 1), (4, 2), (2, 2), (3, 3)]

#     delete_list = combinations(temp_coors,answer)

#     for coors in delete_list:
#         for delete_x, delete_y in coors:
#             area[delete_x][delete_y] = 1
        
#         if bfs(area):
#             print(answer)
#             exit()

#     answer += 1


    
# for i in range(len(black_list)+1):
    
#     delete_list = combinations(black_list,i) # [[(0, 3), (0, 4)], [(0, 3), (0, 7)]

#     for coors in delete_list:
#         # temp = [x[:] for x in area]
#         for delete_x, delete_y in coors:
#             area[delete_x][delete_y] = 1
        
#         if bfs(area):
#             print(i)
#             exit()

#         for delete_x, delete_y in coors:
#             area[delete_x][delete_y] = 0