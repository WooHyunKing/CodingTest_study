def solution(priorities, location):
    answer = 0
    
    queue = [(i,value) for i,value in enumerate(priorities)]
    
    while queue:
        index, priority = queue.pop(0)
        
        if queue and max([x[1] for x in queue]) > priority:
            queue.append((index,priority))
            continue
        
        answer += 1
        
        if index == location:
            return answer
        
    return answer