first = list(input())
second = list(input())

first_len = len(first)
second_len = len(second)

dp = [[0]*(first_len+1) for _ in range(second_len+1)]

for i in range(second_len):
    for j in range(first_len):
        if second[i] == first[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
print(dp[second_len-1][first_len-1])