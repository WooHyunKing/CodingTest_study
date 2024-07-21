def solution(my_string):
    answer = ''
    
    my_string_set = set(list(my_string))
    
    for s in my_string:
        if s in my_string_set:
            answer += s
            my_string_set.discard(s)
    return answer