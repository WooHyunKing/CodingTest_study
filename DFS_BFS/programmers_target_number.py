# BFS
from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque()
    
    queue.append((numbers[0],0))
    queue.append((-numbers[0],0))
    
    while queue:
        v, index = queue.popleft()
            
        index += 1
        
        if index < len(numbers):
            queue.append((v+numbers[index],index))
            queue.append((v-numbers[index],index))
        else:
            if v == target:
                answer += 1
    
    return answer

#DFS
from collections import deque

def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(value, index):
        global answer
            
        if index+1 <= len(numbers):
            dfs(value-numbers[index],index+1)
            dfs(value+numbers[index],index+1)
        else:
            if value == target:
                answer += 1
    dfs(0,0)
    
    return answer
