n, m, dice_x, dice_y, k = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]

move_list = list(map(int,input().split()))

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

# 상단, 남, 동, 서, 북, 하단
dice = [0 for _ in range(6)]

for move in move_list:
    dice_x += dx[move]
    dice_y += dy[move]

    if dice_x < 0 or dice_x >= n or dice_y < 0 or dice_y >=m:
        dice_x -= dx[move]
        dice_y -= dy[move]
        continue

    if move == 1: # 동쪽
        # 상단, 동, 서, 하단 변화
        dice = [dice[3],dice[1] ,dice[0],dice[5],dice[4] ,dice[2]]
    elif move == 2: # 서쪽
        # 상단, 동, 서, 하단 변화
        dice= [dice[2],dice[1] ,dice[5],dice[0],dice[4] ,dice[3]]
    elif move == 3: # 북쪽
        # 상단, 북, 하단, 남 변화
        dice = [dice[1],dice[5], dice[2], dice[3] , dice[0],dice[4]]
    elif move == 4: # 남쪽
        # 상단, 북, 하단, 남 변화
        dice = [dice[4],dice[0], dice[2], dice[3] , dice[5],dice[1]]
        
    if area[dice_x][dice_y] == 0 : # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수를 칸에 복사
        area[dice_x][dice_y] = dice[-1]
    else: # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0
        dice[-1] = area[dice_x][dice_y]
        area[dice_x][dice_y] = 0
    
    print(dice[0])