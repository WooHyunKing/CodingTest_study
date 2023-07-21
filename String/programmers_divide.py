def solution(s):
    answer = []
    
    string = s
    
    while(string != ''):
        x = string[0]
        list_str = list(string)
        
        count_x = 0
        count_not_x = 0
        
        index = 0
        
        for i,value in enumerate(list_str):
            if value == x:
                count_x += 1
            else:
                count_not_x += 1
            
            if count_x != 0 and count_x == count_not_x:
                index = i
                break
            
            index = i
            
        answer.append(list_str[:index+1])
        string = ''.join(list_str[index+1:])
    
    return len(answer)