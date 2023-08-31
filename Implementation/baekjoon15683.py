import copy
n, m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]

# 0은 빈 칸, 6은 벽, 1~5는 CCTV

def monitor_right(x,y,temp_area):
    total = 0
    for i in range(y+1,m):
        if temp_area[x][i] == 6:
            break
        elif temp_area[x][i] == 0:
            temp_area[x][i] = -1
            total += 1
    return total, temp_area

def monitor_left(x,y,temp_area):
    total = 0
    for i in range(y-1,-1,-1):
        if temp_area[x][i] == 6:
            break
        elif temp_area[x][i] == 0:
            temp_area[x][i] = -1
            total += 1
    return total, temp_area

def monitor_top(x,y,temp_area):
    total = 0
    for i in range(x-1,-1,-1):
        if temp_area[i][y] == 6:
            break
        elif temp_area[i][y] == 0:
            temp_area[i][y] = -1
            total += 1
    return total, temp_area

def monitor_down(x,y,temp_area):
    total = 0
    for i in range(x+1,n):
        if temp_area[i][y] == 6:
            break
        elif temp_area[i][y] == 0:
            temp_area[i][y] = -1
            total += 1
    return total, temp_area

def count_blind(result_area):
    total = 0
    for i in range(n):
        for j in range(m):
            if result_area[i][j] == 0:
                total += 1
    return total

cctv_cases= [
    [],
    [['right'],['down'],['left'],['top']],
    [['left','right'], ['top','down']],
    [['top','right'],['right','down'],['down','left'],['left','top']],
    [['left','top','right'],['top','right','down'],['right','down','left'],['down','left','top']],
    [['right','down','left','top']]
]

cctv_list = []

min_value = float("inf")

for i in range(n):
    for j in range(m):
        if area[i][j] != 0 and area[i][j] != 6:
            cctv_list.append((i,j,area[i][j]))

def monitor(start_x,start_y,area,cases):
    for case in cases:
        if case == 'left':
            monitor_left(start_x,start_y,area)
        elif case == 'right':
            monitor_right(start_x,start_y,area)
        elif case == 'top':
            monitor_top(start_x,start_y,area)
        elif case == 'down':
            monitor_down(start_x,start_y,area)

def dfs(depth,area):
    global min_value
    if depth == len(cctv_list):
        min_value = min(min_value,count_blind(area))
        return
    
    cctv_x, cctv_y, value = cctv_list[depth]
    temp_area = copy.deepcopy(area)
    
    for cases in cctv_cases[value]:
        monitor(cctv_x,cctv_y,temp_area,cases)
        dfs(depth+1,temp_area)
        temp_area = copy.deepcopy(area)

dfs(0,area)
print(min_value)