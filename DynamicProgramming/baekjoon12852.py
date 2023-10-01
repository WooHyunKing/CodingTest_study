n = int(input())

dp = [0]*(n+1)

step = [0]*(n+1)

current = n

# if n <= 1:
#     print(dp[n])
#     for i in range(n,0,-1):
#         print()

for i in range(2,n+1):

    dp[i] = dp[i-1] + 1
    step[i] = i-1

    if i % 2 == 0 and dp[i] > (dp[int(i/2)]+1):
        # if dp[i] > dp[int(i/2)]+1:
        #     temp = int(i/2) * 2
        dp[i] = dp[int(i/2)]+1
        step[i] = int(i/2)
        
    if i % 3 == 0 and dp[i] > (dp[int(i/3)]+1):
        # if dp[i] > dp[int(i/3)]+1:
        #     temp = int(i/3) * 3
        dp[i] = dp[int(i/3)]+1
        step[i] = int(i/3)

print(dp[n])
print(step)
while True:
    print(current, end=" ")
    if current == 1:
        break
    current = step[current]
