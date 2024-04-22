# def permutation(arr,r):
    
#     # visited = [False for _ in range(len(arr))]
#     visited = [False]*len(arr)

#     def generate(elements, visited):

#         if len(elements) == r:
#             return [elements[:]]
        
#         cases = []

#         for i in range(len(arr)):
#             if not visited[i]:
#                 visited[i] = True
#                 elements.append(arr[i])
#                 cases.extend(generate(elements,visited))
#                 elements.pop()
#                 visited[i] = False
        
#         return cases
    
#     return generate([],visited)

def permutation(arr,r):

    visited = [False]*len(arr)

    def generate(elements,visited):

        if len(elements) == r:
            return [elements[:]]
        
        cases = []

        for i in range(len(arr)):
            if not visited[i]:
                elements.append(arr[i])
                visited[i] = True
                cases.extend(generate(elements,visited))
                visited[i] = False
                elements.pop()
        
        return cases
    
    return generate([],visited)
        

print(permutation([1,2,3,4,5],3))