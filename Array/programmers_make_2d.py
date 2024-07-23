def solution(num_list, n):
    answer = [[] for _ in range(len(num_list)//n)]
    
    i, j = 0, 0
    
    for num in num_list:
        
        if j == n:
            i += 1
            j = 0
        
        answer[i].append(num)
        j += 1
        
    return answer