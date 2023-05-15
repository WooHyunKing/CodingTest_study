def maxSubarray(arr):
    # Write your code here
    len_arr = len(arr)
    
    dp_array = [0]*(len_arr)
    dp_sequence = [0]*(len_arr)
    
    dp_array[0], dp_sequence[0] = arr[0], arr[0]
    
    for i in range(1,len_arr):
        dp_array[i] = max(arr[i], arr[i]+dp_array[i-1])
        
    for i in range(1,len_arr):
        dp_sequence[i] = max(dp_sequence[i-1], dp_sequence[i-1]+arr[i], arr[i])
        
    return [max(dp_array),dp_sequence[len_arr-1]]