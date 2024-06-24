import sys

input = sys.stdin.readline

# P - 로봇, H - 부품

n, k = map(int,input().split())

area = list(input())

visited = [False]*n

for i,value in enumerate(area):

    if value == 'P':
        for j in range(i-k,i+k+1):
            if 0 <= j < n and not visited[j] and area[j] == 'H':
                if i == j:
                    continue
                visited[j] = True
                break

print(len([x for x in visited if x == True] ))

