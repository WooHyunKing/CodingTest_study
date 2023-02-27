def solution(triangle):
    
    height = len(triangle) # 삼각형의 높이
    
    dp_list = [[0]*height for _ in range(height)]
    
    dp_list[0][0] = triangle[0][0]
    
    for i in range(1,height):
        for j in range(i):
            if (i-1)>=0 and (j-1)>=0:
                dp_list[i][j] = max(dp_list[i-1][j-1]+triangle[i][j], dp_list[i-1][j]+triangle[i][j])
            elif (i-1)>=0 and (j-1)<0:
                dp_list[i][j] = dp_list[i-1][j] + triangle[i][j]
            elif (i-1)<j and (j-1)>=0:
                dp_list[i][j] = dp_list[i-1][j-1] + triangle[i][j]    
            
    max_value = max(dp_list[height-1])

    return max_value