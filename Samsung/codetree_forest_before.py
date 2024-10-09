
area = [[[]]*C for _ in range(R+3)]

# 골렘의 출구 방향 정보 di 는 0과 3 사이의 수로 주어지며 각각의 숫자 0,1,2,3은 북, 동, 남, 서쪽을 의미

def check_floor(x,y):
    if 0 <= x+2 < R + 3 and 0 <= y-1 < C and 0 <= y+1 < C:
        return False
    return True

def check_left(x,y):
    if 0 <= x+2 < R + 3 and 0 <= y-2 < C:
        return True
    return False
def check_right(x,y):
    if 0 <= x+2 < R + 3 and 0 <= y+2 < C:
        return True
    return False


def step_one(x,y,index,d):
    
    if check_floor(x,y):
        return False
    
    if area[x+2][y] != [] or area[x+1][y+1] != [] or area[x+1][y-1] != []:
        return False

    area[x][y] = []
    area[x-1][y] = []
    area[x][y+1] = []
    area[x][y-1] = []
    area[x+1][y] = []

    area[x+2][y] = [x+1,y,index,False]
    area[x+1][y] = [x+1,y,index,False]
    area[x+1][y+1] = [x+1,y,index,False]
    area[x+1][y-1] = [x+1,y,index,False]
    area[x][y] = [x+1,y,index,False]

    if d == 0:
        area[x][y][3] = True
    elif d == 1:
        area[x+1][y+1][3] = True
    elif d == 2:
        area[x+2][y][3] = True
    elif d == 3:
        area[x+1][y-1][3] = True
    # [1,1,0,1] # 행, 열, 골렘 인덱스, 출구 여부

    return x+1,y,index,d

def step_two(x,y,index,d):
    
    if not check_left(x,y):
        return False
    if area[x][y-2] != [] or area[x-1][y-1] != [] or area[x+1][y-1] != [] or area[x+2][y-1] != [] or area[x+1][y-2] != []:
        return False

    area[x][y] = []
    area[x-1][y] = []
    area[x][y+1] = []
    area[x][y-1] = []
    area[x+1][y] = []

    area[x+1][y] = [x+1,y-1,index,False]
    area[x][y-1] = [x+1,y-1,index,False]
    area[x+1][y-1] = [x+1,y-1,index,False]
    area[x+1][y-2] = [x+1,y-1,index,False]
    area[x+2][y-1] = [x+1,y-1,index,False]

    d = (d-1+4)%4

    if d == 0:
        area[x][y-1][3] = True
    elif d == 1:
        area[x+1][y][3] = True
    elif d == 2:
        area[x+2][y-1][3] = True
    elif d == 3:
        area[x+1][y-2][3] = True

    return x+1,y-1,index,d

def step_three(x,y,index,d):
    
    if not check_right(x,y):
        return False
    if area[x][y+2] != [] or area[x-1][y+1] != [] or area[x+1][y+1] != [] or area[x+2][y+1] != [] or area[x+1][y+2] != []:
        return False

    area[x][y] = []
    area[x-1][y] = []
    area[x][y+1] = []
    area[x][y-1] = []
    area[x+1][y] = []

    area[x+1][y] = [x+1,y-1,index,False]
    area[x][y+1] = [x+1,y-1,index,False]
    area[x+1][y+1] = [x+1,y-1,index,False]
    area[x+1][y+2] = [x+1,y-1,index,False]
    area[x+2][y+1] = [x+1,y-1,index,False]

    d = (d-1+4)%4

    if d == 0:
        area[x][y+1][3] = True
    elif d == 1:
        area[x+1][y+2][3] = True
    elif d == 2:
        area[x+2][y+1][3] = True
    elif d == 3:
        area[x+1][y][3] = True

    return x+1,y-1,index,d

def debug():
    for i in area:
        for j in i:
            if j == []:
                print(0, end = " ")
            else:
                print(1, end = " ")
        print()
        
    print()

for index in range(K):
    c, d = map(int,input().split()) # 골렘이 출발하는 열, 골렘의 출구 방향

    x, y = 1, c-1

    debug()

    while True:

        if not check_floor(x,y):
            step_one(x,y,index,d)
            x += 1
            print("1")
            continue

        if check_left(x,y):
            step_two(x,y,index,d)
            x += 1
            y -= 1
            print("2")
            continue

        if check_right(x,y):
            step_three(x,y,index,d)
            x += 1
            y += 1
            print("3")
            continue
        else:
            print("4")
            break
        # if not check_left(x,y):
            
    debug()

    