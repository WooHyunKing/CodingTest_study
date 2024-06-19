import sys

input = sys.stdin.readline

# 헬스장에서 N명의 회원이 운동을 하고 있음
# 각 회원은 1부터 N사이의 번호가 부여

# i번 회원이 들 수 있는 역기의 무게는 Wi

# 회원들 사이에는 M개의 친분 관계 (Aj, Bj)가 있음 (Aj와 Bj가 친분관계)

# i번 회원은 자신과 친분 관계가 있는 다른 회원들보다 들 수 있는 
# 역기의 무게가 무거우면 자신이 최고라고 생각

# 단, 누구와도 친분이 없는 멤버는 본인이 최고라고 생각

N, M = map(int,input().split())

weights = [0] + list(map(int,input().split()))

graph = [[] for _ in range(N+1)]

answer = 0

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):

    if len(graph[i]) == 0:
        answer += 1
        continue

    weight_list = [weights[x] for x in graph[i]]

    if weights[i] > max(weight_list):
        answer += 1
        
print(answer)