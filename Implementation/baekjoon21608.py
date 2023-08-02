n = int(input())

data = [[] for _ in range(n**2)]
location = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

like_dict = {}
sequence = []

total = 0

for i in range(n**2):
    data[i] = list(map(int, input().split()))

for i in range(n**2):
    sequence.append(data[i][0])
    for j in range(1,5):
        if like_dict.get(data[i][0]) == None:
            like_dict[data[i][0]] = {data[i][j]}
        else:
            like_dict[data[i][0]].add(data[i][j])

def getLike(num): # 인접한 좋아하는 학생이 가장 많은 자리 목록 (1번 조건)
    result_list = [] 
    max_value = -1
    for i in range(n):
        for j in range(n):
            if location[i][j] != 0: # 이미 자리가 있는 경우는 pass
                continue
            temp = 0 # 인접한 좋아하는 사람의 수
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if (location[nx][ny] in like_dict[num]):
                        temp += 1
            if (temp > max_value):
                result_list = [(i,j)]
                max_value = temp
            elif (temp == max_value):
                result_list.append((i,j))
    return result_list

def getEmpty(locations): # 인접한 빈칸이 가장 많은 자리 목록 (2번 조건)
    result_list = []
    max_value = -1
    
    for coor in locations:
        temp = 0
        x, y = coor[0], coor[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if location[nx][ny] == 0:
                    temp += 1
        if temp > max_value:
            result_list = [(x,y)]
            max_value = temp
        elif temp == max_value:
            result_list.append((x,y))

    return result_list


def compareRowAndColumn(locations): # 행과 열의 인덱스가 가장 작은 자리 (3번 조건)

    result_list = []
    result = (0,0)
    min_x,min_y = 21, 21
    
    for coor in locations: # 행 구별
        x,y = coor[0], coor[1]
        if x < min_x:
            result_list = [(x,y)]
            min_x = x
        elif x == min_x:
            result_list.append((x,y))
    
    for coor in result_list: # 열 구별
        x,y = coor[0], coor[1]
        if y < min_y:
            result = (x,y)
            min_y = y

    return result

for index in sequence:
    like_list = getLike(index)
    empty_list = getEmpty(like_list)
    final_location = compareRowAndColumn(empty_list)
    x,y = final_location[0], final_location[1]
    location[x][y] = index

for i in range(n):
    for j in range(n):
        index = location[i][j]
        temp = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if location[nx][ny] in like_dict[index]:
                    temp += 1
        if temp == 0:
            total += 0
        elif temp == 1:
            total += 1
        elif temp == 2:
            total += 10
        elif temp == 3:
            total += 100
        elif temp == 4:
            total += 1000

print(total)