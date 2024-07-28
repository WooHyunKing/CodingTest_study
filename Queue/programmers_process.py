# def solution(priorities, location):
#     answer = 0
    
#     queue = [(i,value) for i,value in enumerate(priorities)]
    
#     while queue:
#         index, priority = queue.pop(0)
        
#         if queue and max([x[1] for x in queue]) > priority:
#             queue.append((index,priority))
#             continue
        
#         answer += 1
        
#         if index == location:
#             return answer
        
#     return answer

from collections import deque

def solution(priorities, location):
    answer = 0
    
    sorted_values = sorted(priorities)
    
    priorities = deque([(x,i) for i,x in enumerate(priorities)])
    
    while True:
        
        value, index = priorities.popleft()
        
        if value != sorted_values[-1]:
            priorities.append((value,index))
        else:
            sorted_values.pop()
            answer += 1
            if index == location:
                return answer