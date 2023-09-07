n = int(input())

area = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

count = 0
length = 1
direction = 0

answer = 0

x, y = n//2, n//2

def move(x,y,d):

    global answer 

    total = area[x][y]
    five_percent = int(total * 5 / 100)
    ten_percent = int(total*10/100)
    seven_percent = int(total*7/100)
    one_percent = int(total/100)
    two_percent = int(total*2/100)

    a_x, a_y = x + dx[d], y + dy[d]
    b_x, b_y = x - dx[d], y - dy[d]
    five_x, five_y = x + dx[d]*2, y + dy[d]*2
    
    if d == 0 or d == 2: # 왼쪽이나 오른쪽일 경우
        ten_list = [(a_x-1,a_y), (a_x+1,a_y)]
        seven_list = [(x-1,y),(x+1,y)]
        two_list= [(x-2,y),(x+2,y)]
        one_list = [(b_x-1,b_y),(b_x+1,b_y)]

    elif d == 1 or d == 3: # 위나 아래쪽일 경우
        ten_list = [(a_x,a_y-1), (a_x,a_y+1)]
        seven_list = [(x,y-1),(x,y+1)]
        two_list = [(x,y-2),(x,y+2)]
        one_list = [(b_x,b_y-1),(b_x,b_y+1)]
    
    if 0 <= five_x < n and 0 <= five_y < n:
        area[five_x][five_y] += five_percent
        total -= five_percent
    else:
        answer += five_percent
        total -= five_percent
    
    for ten_x, ten_y in ten_list:
        if 0 <= ten_x < n and 0 <= ten_y < n:
            area[ten_x][ten_y] += ten_percent
            total -= ten_percent
        else:
            answer += ten_percent
            total -= ten_percent
    for seven_x, seven_y in seven_list:
        if 0 <= seven_x < n and 0 <= seven_y < n:
            area[seven_x][seven_y] += seven_percent
            total -= seven_percent
        else:
            answer += seven_percent
            total -= seven_percent
    for two_x, two_y in two_list:
        if 0 <= two_x < n and 0 <= two_y < n:
            area[two_x][two_y] += two_percent
            total -= two_percent
        else:
            answer += two_percent
            total -= two_percent
    
    for one_x, one_y in one_list:
        if 0 <= one_x < n and 0 <= one_y < n:
            area[one_x][one_y] += one_percent
            total -= one_percent
        else:
            answer += one_percent
            total -= one_percent
    
    if 0 <= a_x < n and 0 <= a_y < n:
        area[a_x][a_y] += total
    else:
        answer += total

    area[x][y] = 0
    

while 0 <= x < n and 0 <= y < n:

    count += 1 

    for i in range(length):
        x += dx[direction]
        y += dy[direction]
        if 0 <= x < n and 0 <= y < n:
            move(x,y,direction)

    
    direction = (direction + 1)%4
    
    if count == 2:
        count = 0
        length += 1
        
print(answer)