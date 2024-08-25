def solution(s):
    answer = s
    
    d = dict()
    
    d['zero'],d['one'],d['two'], d['three'],d['four'], d['five'], d['six'], d['seven'], d['eight'], d['nine']   = '0', '1', '2', '3', '4', '5','6','7','8','9'
    
    for key, value in d.items():
        answer = answer.replace(key,value)
    
    return int(answer)