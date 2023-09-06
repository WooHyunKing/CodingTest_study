t = int(input())

def find(row):

    global partial_sum, minimum_sum
    
    if partial_sum > minimum_sum:
        return
    
    if row == n:
        minimum_sum = min(partial_sum,minimum_sum)
        return
    
    for i in range(n):
        if not visited[i]: 
            visited[i] = True
            partial_sum += data[row][i]
            find(row+1)
            visited[i] = False
            partial_sum -= data[row][i]

for tc in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    visited = [False]*n
    
    partial_sum,minimum_sum = 0, float("inf")

    find(0)

    print(f"#{tc+1} {minimum_sum}")

    