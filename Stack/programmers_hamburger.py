def solution(ingredient):
    answer = 0
    
    # 빵 – 야채 – 고기 - 빵
    # 1 - 2 - 3 - 1
    # 빵(1) / 야채(2) / 고기(3)
    
    stack = []
    
    for i in ingredient:
        
        if len(stack) < 3:
            stack.append(i)
            continue
            
        if stack[-3:] == [1,2,3] and i == 1:
            for _ in range(3):
                stack.pop()
            answer += 1
        else:
            stack.append(i)
    
    return answer