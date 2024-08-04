def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[1])
    
    current = -30001
    
    for start, end in routes:
        if start > current:
            answer += 1
            current = end
    
    return answer