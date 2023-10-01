n,m = map(int,input().split())

numbers = list(map(int,input().split()))

answers = []

dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = dp[i-1] + numbers[i-1]

for _ in range(m):
    i, j = map(int,input().split())

    answers.append(dp[j]-dp[i-1])

for answer in answers:
    print(answer)