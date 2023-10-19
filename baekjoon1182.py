n, s = map(int,input().split())

# N개의 정수로 이루어진 수열, 부분수열의 원소를 다 더한 값이 S가 되는 경우의 수

data = list(map(int,input().split()))

count = 0

visited = [False]*n

def dfs(total,index,depth):
    global count

    if total == s and depth != 0:
        count += 1

    for i in range(index,n):
        if not visited[i]:
            visited[i] = True
            dfs(total + data[i], i,depth+1)
            visited[i] = False
    
    # for i,value in enumerate(data):
    #     if i >= depth and not visited[i]:
    #         visited[i] = True
    #         dfs(total + [value],depth+1)
    #         visited[i] = False

dfs(0,0,0)

print(count)