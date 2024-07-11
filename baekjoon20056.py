import sys

input = sys.stdin.readline

# 마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사

# i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si

# 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결

# 파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미

# 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동(이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.)
# 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    # 2-1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    # 2-2. 파이어볼은 4개의 파이어볼로 나누어진다.
    # 2-3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋
        # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
        # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    # 2-4. 질량이 0인 파이어볼은 소멸되어 없어진다.

# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합

n, m, k = map(int,input().split())

dx, dy = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

area = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    ri, ci, mi, si, di  = map(int,input().split())

    area[ri-1][ci-1].append((mi,si,di))

def get_fire_coor(): # 파이어볼이 존재하는 좌표들을 반환하는 함수
    
    coor_list = []

    for i in range(n):
        for j in range(n):
            if len(area[i][j]) != 0:
                coor_list.append((i,j))

    return coor_list

def get_fire_coor_least_two(): # 파이어볼이 2개 이상 존재하는 좌표들을 반환하는 함수
    
    coor_list = []

    for i in range(n):
        for j in range(n):
            if len(area[i][j]) >= 2:
                coor_list.append((i,j))

    return coor_list

def step_one(): # 1번 동작을 수행하는 함수
    
    global area
    
    fire_list = get_fire_coor()

    temp = [[[] for _ in range(n)] for _ in range(n)]

    for x, y in fire_list:
        
        for m, s, d in area[x][y]:

            nx, ny = x + (s%n)*dx[d], y + (s%n)*dy[d]
                

            if nx < 0:
                nx = n - (abs(nx) % (n+1))
            if ny < 0:
                ny = n - (abs(ny) % (n+1))
            if nx >= n:
                nx %= n
            if ny >= n:
                ny %= n

            temp[nx][ny].append((m,s,d))
    
    area = temp

def step_two(): # 2번 동작을 수행하는 함수
    
    least_two_list = get_fire_coor_least_two()

    for x, y in least_two_list:
        
        count = len(area[x][y])
        sum_m = sum([x[0] for x in area[x][y]])
        sum_s = sum([x[1] for x in area[x][y]])
        direction_list = [x[2] for x in area[x][y]]

        after_m, after_s = sum_m // 5, sum_s // count

        even, odd = [], []

        for d in direction_list:

            if d%2 == 0:
                even.append(d)
            else:
                odd.append(d)

        if len(even) == 0 or len(odd) == 0:
            after_d = [0,2,4,6]
        else:
            after_d = [1,3,5,7]

        if after_m != 0 :
            area[x][y] = [(after_m,after_s,d) for d in after_d]
        else:
            area[x][y] = []

def count_all_m(): # 모든 질량을 총합하여 반환하는 함수

    count = 0

    for i in range(n):
        for j in range(n):
            if area[i][j]:
                for m,s,d in area[i][j]:
                    count += m

    return count
                
for _ in range(k):
    step_one()
    step_two()

print(count_all_m())