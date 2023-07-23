def solution(num, total):
    answer = []
    multiple = 0
    
    if num%2 == 0:
        start_num = num//2
        answer = [i for i in range(-(num//2)+1, num//2+1)]
    else:
        start_num = 0
        answer = [i for i in range(-(num//2),num//2+1)]        
    
    while(1):
        if start_num == total:
            answer = [i+multiple for i in answer]
            break
        start_num += num
        multiple += 1
            
    return answer