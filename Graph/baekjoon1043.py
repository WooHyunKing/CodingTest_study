import sys
from itertools import permutations
from collections import deque

input = sys.stdin.readline

# 지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다
# 당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다

# 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다
# 문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것

# 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다

# 당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다

# 사람의 수 N, 그리고 그 이야기의 진실을 아는 사람이 주어진다
# 그리고 각 파티에 오는 사람들의 번호가 주어진다

# 지민이는 모든 파티에 참가해야 한다

# 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램

n, m = map(int,input().split())

know_list = set(list(map(int,input().split()))[1:]) # 1 2 3 4

party = [set() for _ in range(m)]

graph = [set() for _ in range(n+1)]

answer = 0

for i in range(m):
    numbers = list(map(int,input().split()))[1:]
    party[i] = set(numbers)

    if len(numbers) >= 2 :
        path = list(permutations(numbers,2))

        for a,b in path:
            graph[a].add(b)

graph = [list(x) for x in graph]

def bfs(index):

    global know_list

    q = deque([index])

    visited = [False]*(n+1)

    visited[index] = True

    temp = {index}

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                temp.add(i)

    if index in know_list:
        know_list |= temp

for i in range(len(party)):
    for j in party[i]:
        bfs(j)


for i in range(m):
    if not know_list & party[i]:
        answer += 1

print(answer)


# for i in range(m):
#     temp = know_list & party[i]
#     temp2 = party[i] | know_list

#     if temp:
#         know_list = temp2