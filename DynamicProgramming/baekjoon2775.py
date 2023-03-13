# 1 3 6 10
# 1 2 3 4

def dynamic(data):
    floor = data[0]
    index = data[1]

    dp = [[0] * (index+1) for _ in range(floor+1)]
    
    for i in range(1,index+1):
        dp[0][i] = i
    
    for i in range(1,floor+1):
        for j in range(1, index+1):
            if j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[floor][index]

t = int(input())

data = [[0]*2 for _ in range(t)]

for i in range(t):
    for j in range(2):
        data[i][j] = int(input())

for i in data:
    print(dynamic(i))