def dynamic(data):
    n = data[0]
    m = data[1]

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][i] = 1

    for i in range(2,m+1):
        dp[1][i] = i

    for i in range(2, n+1):
        for j in range(i+1,m+1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    
    print(dp[n][m])

t = int(input())

testcase = []

for i in range(t):
    testcase.append(list(map(int,input().split())))

for i in testcase:
    dynamic(i)