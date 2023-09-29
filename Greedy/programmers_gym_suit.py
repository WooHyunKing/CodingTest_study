def solution(n, lost, reserve):
    # 2 <= n <= 30
    # 1 <= len(lost) <= n, 중복 X
    # 1 <= len(reserve) <= n, 중복 X
    
    # 여벌 체육복이 있는 학생만 다른 학생에게 빌려줄 수 있음
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있음
    
    status = [1]*(n+1)
    
    for r in reserve:
        status[r] += 1
        
    for l in lost:
        status[l] -= 1
        
    for i in range(n+1):
        if status[i] == 2:
            if i-1 >= 0 and status[i-1] == 0:
                status[i] -= 1
                status[i-1] += 1
            elif i+1 < n+1 and status[i+1] == 0:
                status[i] -= 1
                status[i+1] += 1
    
    status = status[1:]
    
    return sum([1 for x in status if x != 0 ])