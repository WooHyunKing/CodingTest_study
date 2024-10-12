def combinations_with_repet(arr, k):

    cases = []
    
    def dfs(elements,index):
        
        if len(elements) == k:
            cases.append(elements)
            return
        
        for i in range(index,len(arr)):
            dfs(elements + [arr[i]],i)

    dfs([],0)

    return cases

print(combinations_with_repet([1,2,3],2))