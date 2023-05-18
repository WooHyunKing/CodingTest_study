def gen_combinations(arr,n):
    result = []

    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        element = arr[i]
        rest_arr = arr[i+1:]

        for c in gen_combinations(rest_arr,n-1):
            result.append([element]+c)

    return result

def count_combination(n,k):
    if k == 0:
        return 1
    elif n < k :
        return 0
    else:
        return count_combination(n-1,k-1) + count_combination(n-1,k)
    
print(count_combination(4,2))

print(gen_combinations([1,2,3,4],2))