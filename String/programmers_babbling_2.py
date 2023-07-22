def solution(babbling):
    answer = 0
    prefix_list = ['a','y','w','m']
    
    global current
    current = ''
    
    def check(string):
        
        global current
        
        list_str = list(string)
        
        index = 0
        
        while(index <= len(list_str)-1):
            char = list_str[index]
            
            if current == char:
                current = ''
                return False
            
            if char not in prefix_list:
                current = ''
                return False
            
            if char == 'a':
                temp_string = ''.join(list_str[index:index+3])
                if temp_string != 'aya':
                    current = ''
                    return False
                else:
                    index += 3
            
            elif char == 'y':
                temp_string = ''.join(list_str[index:index+2])
                if temp_string != 'ye':
                    current = ''
                    return False
                else:
                    index += 2
                    
            elif char == 'w':
                temp_string = ''.join(list_str[index:index+3])
                if temp_string != 'woo':
                    current = ''
                    return False
                else:
                    index += 3
                    
                    
            elif char == 'm':
                temp_string = ''.join(list_str[index:index+2])
                if temp_string != 'ma':
                    current = ''
                    return False
                else:
                    index += 2
            current = char
        current = ''
        return True
        
    for i in babbling:
        if check(i):
            answer += 1
    
    return answer