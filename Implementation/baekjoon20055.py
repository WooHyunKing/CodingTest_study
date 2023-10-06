n, k = map(int,input().split())

status = list(map(int,input().split()))

data_top = [0]*n
data_bottom = [0]*n
status_top = status[:n]
status_bottom = list(reversed(status[n:]))

answer = 0

def count_zero(): # 내구성이 0인 칸의 개수를 구하는 함수
    count = 0
    for i in range(n):
        if status_top[i] == 0:
            count += 1
        if status_bottom[i] == 0:
            count += 1
    return count

def rotate(): # 벨트를 한칸 회전하는 함수
    global data_top
    global data_bottom
    global status_top
    global status_bottom
    data_top_poped = data_top.pop()
    data_bottom_poped = data_bottom.pop(0)
    data_top = [data_bottom_poped] + data_top
    data_bottom = data_bottom + [data_top_poped]

    status_top_poped = status_top.pop()
    status_bottom_poped = status_bottom.pop(0)
    status_top = [status_bottom_poped] + status_top
    status_bottom = status_bottom + [status_top_poped]

    if data_top[-1] == 1:
        data_top[-1] = 0

def move(): # 벨트에 올라간 로봇을 이동시키는 함수
    for i in range(len(data_top)-1,-1,-1):
        if i == (len(data_top)-1) and data_top[i] == 1 and data_top[i+1] == 0 and status_top[i+1] >= 1:
            data_top[i] = 0
            status_top[i+1] -= 1
        else:
            if data_top[i] == 1 and data_top[i+1] == 0 and status_top[i+1] >= 1:
                data_top[i+1] = 1
                data_top[i] = 0
                status_top[i+1] -= 1  
    if data_top[-1] == 1:
        data_top[-1] = 0

def put_robot(): # 올리는 위치에 로봇을 올리는 함수
    if data_top[0] == 0 and status_top[0] >= 1:
        data_top[0] = 1
        status_top[0] -= 1

while True:
    answer += 1

    rotate()
    move()
    put_robot()

    if count_zero() >= k:
        break

print(answer)