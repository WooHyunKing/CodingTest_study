# from itertools import combinations

# n = int(input())

# data = [list(map(int,input().split())) for _ in range(n)]

# visited = [False]*(n+1)

# # N은 짝수
# # 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소화

# min_value = float("inf")

# team_set = set()

# for i in range(1,n+1):
#     team_set.add(i)

# def calculate_state(arr): # 팀원들의 능력치의 합을 구하는 함수

#     total = 0

#     cases = list(combinations(arr,2))
#     #print(cases) #[(1, 2), (1, 3), (2, 3)]

#     for one,two in cases:
#         total += (data[one-1][two-1] + data[two-1][one-1])
    
#     return total

# def dfs(start_list):
#     global min_value
#     if len(start_list) == n//2:
#         # print(start_list)
#         # print(team_set-start_list)
#         diff = abs(calculate_state(start_list)-calculate_state(team_set-start_list))
#         min_value = min(min_value,diff)
#         return
    
#     for i in range(1,n+1):
#         if not visited[i] and len(start_list)+1 <= n//2:
#             visited[i] = True
#             start_list.add(i)
#             dfs(start_list)
#             start_list.remove(i)
#             visited[i] = False
#         # if not visited[i] and len(link_list)+1 <= n//2:
#         #     visited[i] = True
#         #     dfs(start_list,link_list+[i])
#         #     visited[i] = False

# empty_set = set()
# dfs(empty_set)
# print(min_value)

n = int(input())

visited = [False for _ in range(n)]

data = [list(map(int, input().split())) for _ in range(n)]

min_value = float("inf")

def dfs(depth,index):
    global min_value

    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += data[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += data[i][j]
        min_value = min(min_value,abs(power1-power2))
        return
    for i in range(index,n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i+1)
            visited[i] = False

dfs(0,0)

print(min_value)
