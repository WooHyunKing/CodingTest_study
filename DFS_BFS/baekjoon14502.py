import copy

def dfs(graph, x, y):
    if graph[x][y] != 2:
        return

    for i in range(4):
        temp_x = x + nx[i]
        temp_y = y + ny[i]

        if temp_x >=0 and temp_x < n and temp_y>=0 and temp_y < m:
            if graph[temp_x][temp_y] == 0:
                graph[temp_x][temp_y] = 2
                dfs(graph,temp_x,temp_y)

def count_safe_area(graph):
    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1

    return count

n, m = map(int,input().split())

area = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

nx = [-1,1,0,0]
ny = [0,0,-1,1]

zero_area = []

max_value = 0

for i in range(n):
    area[i] = list(map(int,input().split()))

for i in range(n):
    for j in range(m):
        if area[i][j] == 0 :
            zero_area.append((i,j))

zero_area_length = len(zero_area)

for i in range(zero_area_length-2):
    for j in range(i+1,zero_area_length-1):
        for k in range(j+1,zero_area_length):
            new_area = copy.deepcopy(area)
            first = new_area[zero_area[i][0]][zero_area[i][1]]
            second = new_area[zero_area[j][0]][zero_area[j][1]]
            third = new_area[zero_area[k][0]][zero_area[k][1]]

            if first == second == third == 0:
                new_area[zero_area[i][0]][zero_area[i][1]] = 1
                new_area[zero_area[j][0]][zero_area[j][1]] = 1
                new_area[zero_area[k][0]][zero_area[k][1]] = 1
            
            for a in range(n):
                for b in range(m):
                    dfs(new_area,a,b)
            
            if count_safe_area(new_area) > max_value:
                max_value = count_safe_area(new_area)

print(max_value)