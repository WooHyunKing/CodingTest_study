# 4x4 크기 보드
# 한번 이동할 때 보드 위에 있는 모든 블록이 상-하-좌-우 중 하나로 이동

# 같은 값을 갖는 두 블록이 충돌하면 합쳐짐
# 한번의 이동에서 합쳐진 블록은 다시 합쳐질 수 X

import copy

n = int(input())

zone = [list(map(int,input().split())) for _ in range(n)]

max_value = -1
# 왼쪽으로 이동시키는 함수
def moveLeft(zone):
    zone = copy.deepcopy(zone)
    marged = [[False]*n for _ in range(n)]
    
    for i in range(n): # 행 
        for j in range(1,n): # 열
            if zone[i][j] == 0:
                continue
            for k in range(j-1,-1,-1):
                if zone[i][k] == zone[i][k+1] and not marged[i][k]:
                    zone[i][k] *= 2
                    zone[i][k+1] = 0
                    marged[i][k] = True
                    break
                elif zone[i][k] == 0:
                    zone[i][k] = zone[i][k+1]
                    zone[i][k+1]= 0 
                else:
                    break

    return zone

def moveRight(zone):
    zone = copy.deepcopy(zone)
    marged = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n-2,-1,-1):
            if zone[i][j] == 0:
                continue
            for k in range(j+1,n):
                if zone[i][k] == zone[i][k-1] and not marged[i][k]:
                    zone[i][k] *= 2
                    zone[i][k-1] = 0
                    marged[i][k] = True
                    break
                elif zone[i][k] == 0:
                    zone[i][k] = zone[i][k-1]
                    zone[i][k-1] = 0
                else:
                    break

    return zone

# 위로 이동시키는 함수
def moveUp(zone):
    zone = copy.deepcopy(zone)
    marged = [[False]*n for _ in range(n)]

    for i in range(n): # 열
        for j in range(1,n): # 행
            if zone[j][i] == 0: # 빈칸인 경우 무시
                continue
            for k in range(j-1,-1,-1): 
                if zone[k][i] == zone[k+1][i] and not marged[k][i]:
                    zone[k][i] *= 2
                    zone[k+1][i] = 0
                    marged[k][i] = True
                    break
                elif zone[k][i] == 0: # 빈칸을 만난 경우
                    zone[k][i] = zone[k+1][i]
                    zone[k+1][i] = 0
                else:
                    break

    return zone
# 아래로 이동시키는 함수
def moveDown(zone):
    zone = copy.deepcopy(zone)
    marged = [[False]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n-2,-1,-1):
            if zone[j][i] == 0:
                continue
            for k in range(j+1,n):
                if zone[k][i] == zone[k-1][i] and not marged[k][i]:
                    zone[k][i] *= 2
                    zone[k-1][i] = 0
                    marged[k][i] = True
                    break
                elif zone[k][i] == 0:
                    zone[k][i] = zone[k-1][i]
                    zone[k-1][i] = 0
                else:
                    break
    return zone

# 최댓값을 찾는 함수
def searchMaxValue(zone):
    global max_value
    for i in range(n):
        for j in range(n):
            if zone[i][j] > max_value:
                max_value = zone[i][j]

def dfs(depth,zone):

    searchMaxValue(zone)
    
    if depth == 5:
        return
    
    dfs(depth+1,moveUp(zone))
    dfs(depth+1,moveDown(zone))
    dfs(depth+1,moveLeft(zone))
    dfs(depth+1,moveRight(zone))

dfs(0,zone)

print(max_value)