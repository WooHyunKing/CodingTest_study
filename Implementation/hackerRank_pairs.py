def pairs(k, arr):
    # Write your code here
    # length = len(arr)
    count = 0
    
    new_set = set(arr)
    
    for ele in arr:
        target_one = ele+k
        target_two = ele-k
        
        if target_one in new_set:
            count += 1
        if target_two in new_set:
            count += 1
            
        new_set.remove(ele)
    
    # for i in range(length):
    #     for j in range(i+1,length):
    #         if abs(arr[i]-arr[j]) == k:
    #              count += 1
    return count