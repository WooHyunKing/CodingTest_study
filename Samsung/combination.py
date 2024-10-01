# def combination(arr,r):
    
#     def generate(elements):
#         if len(elements) == r:
#             return [elements[:]]
        
#         cases = []

#         start = arr.index(elements[-1]) + 1 if elements else 0

#         for i in range(start,len(arr)):
#             elements.append(arr[i])
#             cases.extend(generate(elements))
#             elements.pop()

#         return cases

#     return generate([])

# def combination(arr,r):
    
#     def generate(elements):
        
#         if len(elements) == r:
#             return [elements[:]]
        
#         cases =[]
        
#         start = arr.index(elements[-1]) + 1 if elements else 0

#         for i in range(start,len(arr)):
#             elements.append(arr[i])
#             cases.extend(generate(elements))
#             elements.pop()

#         return cases

#     return generate([])

def combination(arr,k):

    cases = []

    def dfs(elements, index):
        
        if len(elements) == k:
            cases.append(elements)
            return
        
        for i in range(index+1,len(arr)):
            dfs(elements + [arr[i]], i)

    dfs([],-1)

    return cases        

print(combination([1, 2, 3, 4], 3))