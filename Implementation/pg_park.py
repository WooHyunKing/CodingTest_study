def solution(park, routes):
    
    row_l = len(park)
    col_l = len(park[0])
    
    start_location = (0,0)
    
    route_list = []
    
    area = [[""]*col_l for _ in range(row_l)]
    
    for i,row in enumerate(park):
        for j,item in enumerate(row):
            area[i][j] = item
            if item == "S":
                start_location = [i,j]
    
    for i in routes:
        route_list.append((i[0],int(i[2])))
        
    print(area)
        
    for i in route_list:
        d, n = i[0], i[1]
        exist_x = False
        
        if d == "N":
            if (start_location[0] - n) >= 0:
                for j in range(start_location[0]-n,start_location[0]):
                    if area[j][start_location[1]] == "X":
                        exist_x = True
                if not exist_x:
                    start_location[0] -= n
        elif d == "S":
            if (start_location[0] + n) < row_l:
                for j in range(start_location[0],start_location[0]+n+1):
                    if area[j][start_location[1]] == "X":
                        exist_x = True
                if not exist_x:
                    start_location[0] += n
        elif d == "W":
            if (start_location[1] - n) >= 0:
                for j in range(start_location[1]-n,start_location[1]):
                    if area[start_location[0]][j] == "X":
                        exist_x = True
                if not exist_x:   
                    start_location[1] -= n
        elif d == "E":
            if (start_location[1] + n) < col_l:
                for j in range(start_location[1],start_location[1]+n+1):
                    if area[start_location[0]][j] == "X":
                        exist_x = True
                if not exist_x:
                    start_location[1] += n
    
    return start_location