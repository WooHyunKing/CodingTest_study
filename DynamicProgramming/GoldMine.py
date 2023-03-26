t = int(input())

result = []

for i in range(t):
    n, m = map(int,input().split())
    input_data = list(map(int,input().split()))

    max_value = 0
    
    array = [[0]*21 for _ in range(21)]
    dp = [[0]*21 for _ in range(21)]

    for i in range(n):
        for j in range(m):
            array[i][j] = input_data[(i*m)+j]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if j == 1:
                dp[i][j] = array[i-1][j-1]

    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[j][i] = array[j-1][i-1] + max(dp[j-1][i-1],dp[j][i-1],dp[j+1][i-1])

            if dp[j][i] > max_value:
                max_value = dp[j][i]
    
    result.append(max_value)


for i in result:
    print(i)
    