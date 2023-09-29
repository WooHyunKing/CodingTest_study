def solution(answers):
    answer = []
    def method_1(answers):
        inputs = [1,2,3,4,5]*(10000//5 + 1)
        result = [1 for i,value in enumerate(answers) if answers[i] == inputs[i]]
        return sum(result)
    
    def method_2(answers):
        inputs = [2,1,2,3,2,4,2,5]*(10000//8 + 1)
        result = [1 for i,value in enumerate(answers) if answers[i] == inputs[i]]
        return sum(result)
    
    def method_3(answers):
        inputs = [3,3,1,1,2,2,4,4,5,5]*(10000//10 + 1)
        result = [1 for i,value in enumerate(answers) if answers[i] == inputs[i]]
        return sum(result)
    
    answer.append((1, method_1(answers)))
    answer.append((2, method_2(answers)))
    answer.append((3, method_3(answers)))
    
    highest = max([x[1] for x in answer])
    answer = [x[0] for x in answer if x[1]==highest]
    
    return answer