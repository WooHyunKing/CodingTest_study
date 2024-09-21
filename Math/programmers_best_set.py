def solution(n, s):
    answer = []
    
    quo = s//n
    remain = s%n
    
    if n > s:
        return [-1]
    
    answer = [quo]*n
    
    for i in range(remain):
        answer[i] += 1
    
    answer.sort()
    
    return answer