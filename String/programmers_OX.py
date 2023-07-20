def solution(quiz):
    answer = []
    for i in quiz:
        
        data = i.split()
        
        result = int(data[-1])
        
        formula = ''.join(data[:-2])
        
        if eval(formula) == result:
            answer.append("O")
        else:
            answer.append("X")
            
    return answer