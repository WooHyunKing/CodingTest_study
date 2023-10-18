n, m = map(int,input().split())

card_list = list(map(int,input().split()))

visited = [False]*n

min_diff = float("inf")

def dfs(total,count):

    global min_diff
    global answer

    diff = m - total
    
    if count == 3:
        if diff >= 0 and diff < min_diff:
            min_diff = diff
            answer = total
        return
    
    for i,value in enumerate(card_list):
        if not visited[i]:
            visited[i] = True
            dfs(total+value,count+1)
            visited[i] = False

dfs(0,0)

print(answer)