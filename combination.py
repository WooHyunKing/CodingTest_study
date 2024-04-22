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

def combination(arr,r):
    
    def generate(elements):
        
        if len(elements) == r:
            return [elements[:]]
        
        cases =[]
        
        start = arr.index(elements[-1]) + 1 if elements else 0

        for i in range(start,len(arr)):
            elements.append(arr[i])
            cases.extend(generate(elements))
            elements.pop()

        return cases

    return generate([])


print(combination([1, 2, 3, 4, 5], 2))