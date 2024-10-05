import sys
import copy

input = sys.stdin.readline

# NxN 크기의 공간에 선생님(T), 학생(S), 혹은 장애물(O)이 위치
# 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표

# 각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행
# 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다
# 단, 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다

# 학생들은 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치
# 결과적으로 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 계산

# 출력 : 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 여부

N = int(input())

area = [list(input().split()) for _ in range(N)]

empty_list = []
t_list = []
s_list = []

for i in range(N):
    for j in range(N):
        if area[i][j] == 'X':
            empty_list.append((i,j))
        elif area[i][j] == 'T':
            t_list.append((i,j))
        elif area[i][j] == 'S':
            s_list.append((i,j))

def combinations(arr,k):

    cases = []

    def dfs(coors,index):

        if len(coors) == k:
            cases.append(coors)
            return

        for i in range(index+1,len(arr)):
            dfs(coors+[arr[i]],i)
            
    dfs([],-1)

    return cases

cases = combinations(empty_list,3)

def check(area):

    visited = [[False]*N for _ in range(N)]

    flag = True

    for x, y in t_list:

        for nx in range(x+1,N): # 남쪽
            if area[nx][y] == 'O':
                break
            if area[nx][y] == 'S':
                visited[nx][y] = True
        for nx in range(x-1,-1,-1): # 북쪽
            if area[nx][y] == 'O':
                break
            if area[nx][y] == 'S':
                visited[nx][y] = True
        for ny in range(y+1,N): # 동쪽
            if area[x][ny] == 'O':
                break
            if area[x][ny] == 'S':
                visited[x][ny] = True
        for ny in range(y-1,-1,-1): # 서쪽
            if area[x][ny] == 'O':
                break
            if area[x][ny] == 'S':
                visited[x][ny] = True
    for x, y in s_list:
        if visited[x][y]:
            flag = False
            break
            
    return flag

for case in cases:

    new_area = copy.deepcopy(area)

    for x, y in case:
        new_area[x][y] = 'O'

    if check(new_area):
        print("YES")
        exit()

print("NO")