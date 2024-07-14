def solution(m, n, puddles):
    
    # m x n 크기의 격자모양
    # 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다
    # 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지
    
    # 0 1 1 1
    # 1 0 1 2
    # 1 1 2 4
    
    area = [[0]*m for _ in range(n)]
    
    for x, y in puddles:
        area[y-1][x-1] = 1
        
    dp = [[0]*m for _ in range(n)]
    
    for i in range(1,n):
        if area[i][0] == 0:
            dp[i][0] = 1
        else:
            break
    for i in range(1,m):
        if area[0][i] == 0:
            dp[0][i] = 1
        else:
            break
        
    for i in range(1,n):
        for j in range(1,m):
            if area[i][j] == 0:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
            else:
                dp[i][j] = 0

    return dp[n-1][m-1]