def solution(answers):
    answer = []
    
    results = [0]*4
    
    one = [1,2,3,4,5]*(10000//5)
    two = [2,1,2,3,2,4,2,5]*(10000//8)
    three = [3,3,1,1,2,2,4,4,5,5]*(10000//10)
    
    for i,ans in enumerate(answers):
        if one[i] == ans:
            results[1] += 1
        if two[i] == ans:
            results[2] += 1
        if three[i] == ans:
            results[3] += 1
            
    maximum_value = max(results)
    
    for i in range(1,4):
        if results[i] == maximum_value:
            answer.append(i)
    
    return answer