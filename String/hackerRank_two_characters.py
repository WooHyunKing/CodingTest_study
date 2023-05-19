def alternate(s):
    # Write your code here
    result_list = []
    
    def gen_comb(arr,n):
        result = []
        if n == 0:
            return [[]]
        for i in range(len(arr)):
            element = arr[i]
            rest_arr = arr[i+1:]
            
            for c in gen_comb(rest_arr,n-1):
                result.append([element]+c)
                
        return result
        
    def validate(arr):
        length = len(arr)
        if length >=2:
            first, second = arr[0],arr[1]
            for j in range(length):
                if j%2 == 0 and arr[j] != first:
                    return False
                if j%2 == 1 and arr[j] != second:
                    return False
            return True
        else:
            return True

    char_list = list(s) # [b,e,a,b,e,e,f,e,a,b]
    char_set = set(char_list) # {a,b,e,f}
    
    set_to_arr = list(char_set) # [a,b,e,f]
    
    com_list = gen_comb(set_to_arr,2)
    #[['a', 'b'], ['a', 'e'], ['a', 'f'], ['b', 'e'], ['b', 'f'], ['e', 'f']]
    
    for i in com_list: # ['a','b']
        temp_string = char_list.copy() # [b,e,a,b,e,e,f,e,a,b]
        append_string = [] 
        for j in range(len(temp_string)):
            if temp_string[j] in i:
                append_string.append(temp_string[j])
        result_list.append(append_string)
        
    result_list = [x for x in result_list if validate(x)]
    #[['b', 'e', 'b', 'e', 'e', 'e', 'b'], ['b', 'a', 'b', 'a', 'b'], ['e', 'a', 'e', 'e', 'e', 'a'], ['b', 'b', 'f', 'b'], ['e', 'e', 'e', 'f', 'e'], ['a', 'f', 'a']]

    result = [len(x) for x in result_list]
    if len(result) >= 1:
        solution = max(result)
    else:
        solution = 0
        
    return solution