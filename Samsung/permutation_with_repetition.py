def permutation_with_repet(arr, k):
    
    cases = []

    def dfs(elements):
        
        if len(elements) == k:
            cases.append(elements)
            return
        
        for i in range(len(arr)):
            dfs(elements + [arr[i]])
    
    dfs([])

    return cases

print(permutation_with_repet([1,2,3],2))