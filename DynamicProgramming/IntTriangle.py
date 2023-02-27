def solution(triangle):
    
    height = len(triangle) # 삼각형의 높이
    
    dp_list = [[0]*height for _ in range(height)]
    
    dp_list[0][0] = triangle[0][0]
    
    for i in range(1,height):
        for j in range(len(triangle[i])):
            if j==0:
                dp_list[i][j] = dp_list[i-1][0] + triangle[i][0]
            elif i==j:
                dp_list[i][j] = dp_list[i-1][j-1] + triangle[i][j] 
            
            else:
                dp_list[i][j] = max(dp_list[i-1][j-1]+triangle[i][j], dp_list[i-1][j]+triangle[i][j])
               
    max_value = max(dp_list[-1])

    return max_value