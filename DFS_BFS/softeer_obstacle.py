import sys

n = int(input())

area = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]

count = 0
count_list = []

nx = [-1,1,0,0]
ny = [0,0,-1,1]

for i in range(n):
    input_row = list(input())
    area[i] = [int(value) for value in input_row]

def dfs(x,y):
    global count

    if area[x][y] == 0 or visited[x][y]:
        return False

    visited[x][y] = True
    count += 1
    
    for i in range(4):
        temp_x = x + nx[i]
        temp_y = y + ny[i]

        if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < n and not visited[temp_x][temp_y]:
            if area[temp_x][temp_y] == 1:
                    dfs(temp_x,temp_y)
    return True

for i in range(n):
    for j in range(n):
        if dfs(i,j):
            count_list.append(count)
            count = 0
print(len(count_list))
for i in sorted(count_list):
    print(i)