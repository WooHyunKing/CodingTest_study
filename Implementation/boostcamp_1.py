def getDuplicate(arr):
    result = []
    
    set_arr = set(arr)
    
    for i in arr:
        if (i in set_arr) and (arr.count(i) > 1):
            result.append(arr.count(i))
            set_arr.remove(i)

    if len(result) == 0:
        return [-1]
    else:
        return result
    

input_value = list(map(int,input().split()))

print(getDuplicate(input_value))
        