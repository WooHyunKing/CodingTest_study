def solution(survey, choices):
    answer = ''
    
    # 검사 결과는 모든 질문의 성격 유형 점수를 더하여 각 지표에서 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형이라고 판단
    # 단, 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단
    
    keys = [['R','T'], ['C','F'],['J','M'],['A','N']]
    
    for i in range(len(keys)):
        keys[i].sort()
    
    dictionary = dict()
    
    dictionary['R'], dictionary['T'], dictionary['C'], dictionary['F'], dictionary['J'], dictionary['M'], dictionary['A'], dictionary['N'] = 0, 0, 0, 0, 0, 0, 0, 0
    
    for i,s in enumerate(survey):
        if choices[i] > 4:
            dictionary[s[1]] += (choices[i]%4)
        elif choices[i] < 4:
            dictionary[s[0]] += (4-choices[i])
    
    for left, right in keys:
        
        if dictionary[left] > dictionary[right]:
            answer += left
        elif dictionary[left] < dictionary[right]:
            answer += right
        else:
            answer += left
    
    return answer