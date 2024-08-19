def solution(array):
    answer = 0
    
    d = dict()
    
    for a in array:
        if a not in d:
            d[a] = 1
        else:
            d[a] += 1
    
    value_list = list(d.items())
    
    maximum = max(value_list,key=lambda x:x[1])[1]
    answer =[x for x in value_list if x[1] == maximum]
    
    if len(answer) >= 2:
        return -1
    
    return answer[0][0]