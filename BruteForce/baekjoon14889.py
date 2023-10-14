n = int(input())

data = [list(map(int,input().split())) for _ in range(n)]

print(data)

min_value = float("inf")

def dfs(start_list,link_list):

    global min_value
    
    if len(start_list) == n//2 and len(link_list) == n//2:
        if abs(sum(start_list) - sum(link_list)) < min_value:
            min_value = abs(sum(start_list) - sum(link_list))
        return
    
    