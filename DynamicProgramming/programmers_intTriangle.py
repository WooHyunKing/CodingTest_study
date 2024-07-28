# def solution(triangle):
    
#     height = len(triangle) # 삼각형의 높이
    
#     dp_list = [[0]*height for _ in range(height)]
    
#     dp_list[0][0] = triangle[0][0]
    
#     for i in range(1,height):
#         for j in range(len(triangle[i])):
#             if j==0:
#                 dp_list[i][j] = dp_list[i-1][0] + triangle[i][0]
#             elif i==j:
#                 dp_list[i][j] = dp_list[i-1][j-1] + triangle[i][j] 
            
#             else:
#                 dp_list[i][j] = max(dp_list[i-1][j-1]+triangle[i][j], dp_list[i-1][j]+triangle[i][j])
               
#     max_value = max(dp_list[-1])

#     return max_value

# def solution(triangle):
    
#     n = len(triangle)
    
#     dp = [[0]*n for _ in range(n)]
#     dp[0][0] = triangle[0][0]
    
#     for i in range(1,n):
#         width = len(triangle[i])
#         for j in range(width):
#             if j == 0:
#                 dp[i][j] = dp[i-1][j] + triangle[i][j]
#             elif j == (width-1):
#                 dp[i][j] = dp[i-1][j-1] + triangle[i][j]
#             else:
#                 dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                
#     return max(dp[-1])

def solution(triangle):
    
    length = len(triangle)
    
    tri = dp = [[0]*(length) for _ in range(length)]
    dp = [[0]*(length) for _ in range(length)]
    
    for i, row in enumerate(triangle):
        for j, value in enumerate(row):
            tri[i][j] = value
    
    dp[0][0] = tri[0][0]
    
    for i in range(1,length):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + tri[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + tri[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]
    
    return max(dp[-1])