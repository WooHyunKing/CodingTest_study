from collections import deque

def solution(progresses, speeds):
    answer = []
    
    length = len(progresses)
    
    while len(progresses) > 0:
        
        count = 0
        
        remain = 100-progresses[0]
        
        if remain%speeds[0] != 0:
            remain = remain // speeds[0] + 1
        else:
            remain = remain // speeds[0]
        
        progresses = [value+(remain*speeds[i]) for i,value in enumerate(progresses)]
        
        for item in progresses:
            if item >= 100:
                count += 1
            else:
                break
        
        for _ in range(count):
            progresses.pop(0)
            speeds.pop(0)
            
        answer.append(count)
        
    return answer