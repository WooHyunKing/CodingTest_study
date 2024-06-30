# n, m = map(int,input().split())

# is_used = [False]*9

# temp = []

# answer = []

# def backtracking():
    
#     if len(temp) == m:
#         answer.append(' '.join(map(str,temp)))
#         return
#     for i in range(1,n+1):
#         if not is_used[i]:
#             is_used[i] = True
#             temp.append(i)
#             backtracking()
#             is_used[i]= False
#             temp.pop()

# backtracking()   

# for ans in answer:
#     print(ans)

import sys

input = sys.stdin.readline

n, m = map(int,input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

answer = []

visited = [False]*(n+1)

def dfs(numbers):
    
    if len(numbers) == m:
        answer.append(numbers)
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            dfs(numbers+[i])
            visited[i] = False

dfs([])

for ans in answer:
    for n in ans:
        print(n,end=" ")
    print()