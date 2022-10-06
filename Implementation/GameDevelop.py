n, m = map(int,input().split())

x, y, d = map(int,input().split())

coor = []

count = 1

for i in range(n):
    row = list(map(int,input().split()))
    coor.append(row)

while True:

    coor[x][y] = 1

    if ((coor[x][y-1] == 1)and(coor[x][y+1] == 1) and (coor[x-1][y] == 1) and (coor[x+1][y] == 1)):
        break

    if d == 0 : # 북쪽인 경우
        if coor[x][y-1] == 0: # 서쪽 방향
            y -= 1
            count += 1
            d = 3
            continue
        elif coor[x+1][y] == 0: # 남쪽 방향
            x += 1
            count += 1
            d = 2
            continue
        elif coor[x][y+1] == 0: # 동쪽 방향
            y += 1
            count += 1
            d = 1
            continue
        else : # 북쪽 방향
            x -= 1
            count += 1

    elif d == 1 : # 동쪽인 경우
        if coor[x-1][y] == 0: # 북쪽 방향
            x -= 1
            count += 1
            d = 0
            continue
        elif coor[x][y-1] == 0: # 서쪽 방향
            y -= 1
            count += 1
            d = 3
            continue
        elif coor[x+1][y] == 0: # 남쪽 방향
            x += 1
            count += 1
            d = 2
            continue
        else : # 동쪽 방향
            y += 1
            count += 1

    elif d == 2 : # 남쪽인 경우
        if coor[x][y+1] == 0: # 동쪽 방향
            y += 1
            count += 1
            d = 1
            continue
        elif coor[x-1][y] == 0: # 북쪽 방향
            x -= 1
            count += 1
            d = 0
            continue
        elif coor[x][y-1] == 0: # 서쪽 방향
            y -= 1
            count += 1
            d = 3
            continue
        else : # 남쪽 방향
            x += 1
            count+=1

    elif d == 3 : # 서쪽인 경우
        if coor[x+1][y] == 0: # 남쪽 방향
            x += 1
            count += 1
            d = 2
            continue
        elif coor[x][y+1] == 0: # 동쪽 방향
            y += 1
            count += 1
            d = 1
            continue
        elif coor[x-1][y] == 0: # 북쪽 방향
            x -= 1
            count += 1
            d = 0
            continue
        else: # 서쪽 방향
            y -= 1
            count+=1

print(count)




        

