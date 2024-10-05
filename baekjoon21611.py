import sys
from collections import deque

input = sys.stdin.readline

# 가장 처음에 상어가 있는 칸을 제외한 나머지 칸에는 구슬이 하나 들어갈 수 있다
# 구슬은 1번 구슬, 2번 구슬, 3번 구슬이 있다

# 같은 번호를 가진 구슬이 번호가 연속하는 칸에 있으면, 그 구슬을 연속하는 구슬이라고 한다.

# 블리자드 마법을 시전하려면 방향 di와 거리 si를 정해야 한다. 
# 총 4가지 방향 ↑, ↓, ←, → (1, 2, 3, 4)

# 마법사 상어는 블리자드를 총 M번 시전
# 시전한 마법의 정보가 주어졌을 때

# 출력 : 폭발한 1번 구슬의 개수, 폭발한 2번 구슬의 개수, 폭발한 3번 구슬의 개수

N, M = map(int,input().split())

# r번째 행의 c번째 정수는 (r, c)에 들어있는 구슬의 번호를 의미
# 어떤 칸에 구슬이 없으면 0, 상어가 있는 칸도 항상 0
area = [list(map(int,input().split())) for _ in range(N)]

boom_one, boom_two, boom_three = 0, 0, 0

dx = [0,1,0,-1]
dy = [-1,0,1,0]

answer_1, answer_2, answer_3 = 0, 0, 0

# 1) 구슬 파괴
# 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴
# 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸이 된다.
# 총 4가지 방향 ↑, ↓, ←, → (1, 2, 3, 4)

def delete(d,s,x,y):
    if d == 1:
        for i in range(x-1,x-(s+1),-1):
            area[i][y] = 0
    elif d == 2:
        for i in range(x+1,x+(s+1)):
            area[i][y] = 0
    elif d == 3:
        for j in range(y-1,y-(s+1),-1):
            area[x][j] = 0
    elif d == 4:
        for j in range(y+1,y+(s+1)):
            area[x][j] = 0

# 2) 구슬 앞당기기
# 만약 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동

def get_numbers(): # 구슬을 순서대로 반환하는 함수

    x, y = N//2, N//2

    length = 1
    turn_count = 0
    d_index = 0

    result = []

    while 0 <= x < N and 0 <= y < N:
        

        for _ in range(length):
            x += dx[d_index]
            y += dy[d_index]
            if 0 <= x < N and 0 <= y < N and area[x][y] != 0:
                result.append(area[x][y])

        d_index = (d_index + 1)%4
        
        turn_count += 1

        if turn_count == 2:
            turn_count = 0
            length += 1

    return result

def create_new_area(values): # 주어진 순서대로 구슬을 채워서 반환하는 함수

    new_area = [[0]*N for _ in range(N)]
    q = deque(values)

    x, y = N//2, N//2

    length = 1
    turn_count = 0
    d_index = 0

    while 0 <= x < N and 0 <= y < N:
        for _ in range(length):
            x += dx[d_index]
            y += dy[d_index]
            if q:
                new_area[x][y] = q.popleft()
            else:
                break
        if not q:
            break

        d_index = (d_index+1)%4
        turn_count += 1

        if turn_count == 2:
            turn_count = 0
            length += 1
            
    return new_area

# 3) 구슬 폭발 + 구슬 앞당기기 (더 이상 폭발하는 구슬이 없을 때 까지 반복)
# 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생
            
def boom(): # 구슬을 폭발시키는 함수

    global answer_1, answer_2, answer_3

    numbers = get_numbers()

    count = 0

    result = []

    temp = []

    for i in range(len(numbers)):
        if i == 0:
            count += 1
            temp.append(numbers[i])
        elif i == (len(numbers)-1):
            if numbers[i-1] != numbers[i]:
                if count < 4:
                    result += temp
                else:
                    if numbers[i-1] == 1:
                        answer_1 += count
                    elif numbers[i-1] == 2:
                        answer_2 += count
                    elif numbers[i-1] == 3:
                        answer_3 += count
                temp = [numbers[i]]
                result += temp
            else:
                count += 1
                temp.append(numbers[i])
                if count < 4:
                    result += temp
                else:
                    if numbers[i] == 1:
                        answer_1 += count
                    elif numbers[i] == 2:
                        answer_2 += count
                    elif numbers[i] == 3:
                        answer_3 += count
                temp = []
                        
        else:
            if numbers[i-1] != numbers[i]:
                if count < 4:
                    result += temp
                else:
                    if numbers[i-1] == 1:
                        answer_1 += count
                    elif numbers[i-1] == 2:
                        answer_2 += count
                    elif numbers[i-1] == 3:
                        answer_3 += count
                temp = [numbers[i]]
                count = 1
            else:
                count += 1
                temp.append(numbers[i])

    if len(numbers) == len(result) : # 폭발이 없는 경우
        return []
    else:
        return result

# 4) 구슬 변화
# 연속하는 구슬은 하나의 그룹
# 하나의 그룹은 두 개의 구슬 A(그룹에 들어있는 구슬의 개수)와 B(그룹을 이루고 있는 구슬의 번호)로 변한다
# 구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서로 칸에 들어간다.
# 만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다.

def change(): # 구슬을 변화시키는 함수
    numbers = get_numbers()

    temp = []

    result = []

    for i in range(len(numbers)):
        if i == 0:
            temp.append(numbers[i])
        elif i == (len(numbers)-1):
            if numbers[i-1] != numbers[i]:
                result += [len(temp),numbers[i-1]]
                temp = [numbers[i]]
                result += [len(temp),numbers[i]]
            else:
                temp.append(numbers[i])
                result += [len(temp),numbers[i]]
        else:
            if numbers[i-1] != numbers[i]:
                result += [len(temp),numbers[i-1]]
                temp = [numbers[i]]
            else:
                temp.append(numbers[i])

    return result[:N*N-1]
                
for _ in range(M):
    d, s = map(int,input().split())

    delete(d,s,N//2,N//2)

    area = create_new_area(get_numbers())

    while True:
        boom_result = boom()
    
        if not boom_result:
            break
    
        area = create_new_area(boom_result)

    change_result = change()
    
    area = create_new_area(change_result)

print(answer_1 + 2*answer_2 + 3*answer_3,end="")