import sys

input = sys.stdin.readline

n, k, m = map(int,input().split())

values = [(0,0)]+ [tuple(map(int,input().split())) for _ in range(n)]

answer = 0

visited = [False]*(n+1)

for _ in range(k):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp_set = [[set()]*(m+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        weight = values[i][0]
        price = values[i][1]

        for j in range(1,m+1):
            if visited[i]:
                dp[i][j] = dp[i-1][j]
                dp_set[i][j] = dp_set[i-1][j]
                continue
            if j >= weight:
                select =  dp[i][j-weight]+price
                not_select = dp[i-1][j]

                print(weight,price)
                print(i,j)
                print("select : ",select)
                print("not_select : ",not_select)


                if select > not_select:
                    dp[i][j] = select
                    dp_set[i][j] = dp_set[i-1][j-weight] | {i}
                elif select == not_select:
                    temp = dp_set[i][j-weight] | {i}
                    temp2 = dp_set[i-1][j]
                    if len(temp) >  len(temp2):
                        dp[i][j] = not_select
                        dp_set[i][j] = dp_set[i-1][j]
                    else:
                        dp[i][j] = select
                        dp_set[i][j] = dp_set[i-1][j-weight] | {i}
                else:
                    dp[i][j] = dp[i-1][j]
                    dp_set[i][j] = dp_set[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
                dp_set[i][j] = dp_set[i-1][j]

    for i in dp:
        print(i)

    for i in dp_set:
        print(i)
    print()
    answer += dp[n][m]
    for i in dp_set[n][m]:
        visited[i] = True

    print(visited)

print(answer)
        