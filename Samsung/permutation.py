def permutations(arr, k):
    cases = []
    visited = [False]*(len(arr))

    def dfs(elements):
        
        if len(elements) == k:
            cases.append(elements)
            return
        
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                dfs(elements + [arr[i]])
                visited[i] = False
    
    dfs([])

    return cases

print(permutations([1,2,3],2))
        
    
    
    