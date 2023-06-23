def solution(wallpaper):
    
    left_top = [49,49]
    right_down = [0,0]
    
    row_l, col_l = len(wallpaper), len(wallpaper[0])
    
    area = [[""]*col_l for _ in range(row_l)]
    
    for i,row in enumerate(wallpaper):
        for j,item in enumerate(row):
            area[i][j] = item
            if item == "#":
                left_top[0] = min(left_top[0],i)
                left_top[1] = min(left_top[1],j)
                right_down[0] = max(right_down[0],i+1)
                right_down[1] = max(right_down[1],j+1)

    return left_top + right_down