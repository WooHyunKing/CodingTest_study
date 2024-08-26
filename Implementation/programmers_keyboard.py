def solution(keymap, targets):
    answer = []
    
    # 휴대폰 자판은 키의 개수가 1개부터 최대 100개
    # 특정 키를 눌렀을 때 입력되는 문자들도 무작위로 배열
    
    # 휴대폰 자판을 이용해 특정 문자열을 작성할 때, 키를 최소 몇 번 눌러야 그 문자열을 작성할 수 있는지 알아보고자 합니다.
    
    # 단, 목표 문자열을 작성할 수 없을 때는 -1을 저장
    
    d = dict()
    
    for string in keymap:
        for i, alpha in enumerate(string):
            if alpha in d:
                if d[alpha] > i+1:
                    d[alpha] = i+1
            else:
                d[alpha]= i+1
    
    for string in targets:
        
        count = 0
        
        for alpha in string:
            if alpha not in d:
                count = -1
                break 
            else:
                count += d[alpha]
        
        answer.append(count)
    
    return answer