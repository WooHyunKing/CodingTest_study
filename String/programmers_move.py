def solution(A, B):
    
    def move(string):
        list_str = list(string)
        str_len = len(list_str)
        
        new_list = [list_str[-1]] + list_str[:-1]
        
        print(new_list)
        
        return ''.join(new_list)
    
    available = False
    check_str = A
    
    answer = 0
    
    for i in range(len(A)):
        if check_str == B:
            available = True
            break
        check_str = move(check_str)
        answer += 1
    
    if available:
        return answer
    else:       
        return -1