def solution(my_string):
    answer = 0
    num_list = ("0","1","2","3","4","5","6","7","8","9")
    temp_str = ''
    
    for value in my_string:
        if value in num_list:
            temp_str += value
        else:
            if temp_str != '':
                answer += int(temp_str)
                temp_str = ''
                
    if temp_str != '':
        answer += int(temp_str)

    return answer