gear = [[0]*8 for _ in range(4)]
rotate_list = []

score = 0

for i in range(4):
    gear[i] = list(map(int,list(input())))

def rotate_right(lst): # 시계 방향으로 회전시키는 함수
    lst.insert(0,lst.pop())

def rotate_left(lst): # 반시계 방향으로 회전시키는 함수
    lst.append(lst.pop(0))    

k = int(input())

for i in range(k): # 회전 목록 입력받고 저장
    number, direction = map(int,input().split())
    rotate_list.append((number-1,direction,"both"))

def rotate(index,d): # 주어진 방향으로 회전시키는 함수
    if d == 1:
        rotate_right(gear[index])
    elif d == -1:
        rotate_left(gear[index])

def propagation(n,direct,prop_direct): # 회전 전파시키는 함수

    if prop_direct == "both": # 회전 전파 방향이 양쪽 일때
        if n - 1 >= 0 and gear[n][6] != gear[n-1][2]: # 서로 극이 다른 경우 왼쪽으로 전파(재귀방식)
            propagation(n-1,-direct,"left")
            
        if n + 1 < 4 and gear[n][2] != gear[n+1][6]: # 서로 극이 다른 경우 오른쪽으로 전파(재귀방식)
            propagation(n+1,-direct,"right")
        
    elif prop_direct == "left": # 회전 전파 방향이 왼쪽 일때
        if n - 1 >= 0 and gear[n][6] != gear[n-1][2]: # 서로 극이 다른 경우 왼쪽으로 전파(재귀방식)
            propagation(n-1,-direct,"left")

    elif prop_direct == "right": # 회전 전파 방향이 오른쪽 일때
        if n + 1 < 4 and gear[n][2] != gear[n+1][6]: # 서로 극이 다른 경우 오른쪽으로 전파(재귀방식)
            propagation(n+1,-direct,"right")

    rotate(n,direct) # 회전

for gear_index,rotate_d, rotate_prop in rotate_list:
    propagation(gear_index,rotate_d,rotate_prop)

for i in range(4): # 점수 계산
    if i == 0 and gear[i][0] == 1:
        score += 1
    elif i == 1 and gear[i][0] == 1:
        score += 2
    elif i == 2 and gear[i][0] == 1:
        score += 4
    elif i == 3 and gear[i][0] == 1:
        score += 8

print(score)