import sys
sys.setrecursionlimit(10**7)
n = int(input())

# X의 크기는 8보다 작거나 같은 자연수
# X의 원소는 0보다 크거나 같고 16보다 작거나 같은 정수이다.

# 사전 순으로 가장 빠른 것

x = sorted(list(map(int,input().split())))

s = [-1 for _ in range(n*2)]
visited = [False for _ in range(17)]

def dfs(index):

    if index == n*2:
        for i in s:
            print(i,end=" ")
        exit(0)

    if s[index] != -1: # 이미 원소가 있다면 다음 인덱스 체크
        dfs(index+1)
        return

    for i in range(n):
        num = x[i] # 원소 값
        next_index = index + num + 1 # 현재 인덱스 + 원소 값 + 1
        if not visited[num]: # 해당 원소가 아직 사용되지 않았다면
            if 0<= next_index < n*2 and s[next_index] == -1:
                s[index] = num
                s[next_index] = num
                visited[num] = True
                dfs(index+1)
                s[index] = -1
                s[next_index] = -1
                visited[num] = False

dfs(0)

print(-1)