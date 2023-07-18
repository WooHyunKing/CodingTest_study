def solution(babbling):
    answer = 0
    
    available = ('aya','ye','woo','ma')
    available_prefix = ('a','y','w','m')
    
    def checkFunc(arr):
        arr_length = len(arr)
        i = 0
    
        while(i <= arr_length-1):
            value = arr[i]
            
            if value not in available_prefix:
                return False
            
            if value == 'a':
                if arr[i:i+3] != 'aya':
                    return False
                else:
                    i += 3
            
            if value == 'y':
                if arr[i:i+2] != 'ye':
                    return False
                else:
                    i += 2
                    
            if value == 'w':
                if arr[i:i+3] != 'woo':
                    return False
                else:
                    i += 3
                
            if value == 'm':
                if arr[i:i+2] != 'ma':
                    return False
                else:
                    i += 2
                
        return True
    
    for i in babbling:
        if checkFunc(i):
            answer += 1
            
    return answer