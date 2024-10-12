def combinations(arr, k):

    cases = []

    def dfs(elements,index):

        if len(elements) == k:
            cases.append(elements)
            return

        for i in range(index+1,len(arr)):
            dfs(elements + [arr[i]],i)

    dfs([],-1)

    return cases    

# def combination_with_replacement(arr, k):
#     cases = []

#     def dfs(elements, index):
#         if len(elements) == k:
#             cases.append(elements)
#             return
        
#         for i in range(index, len(arr)):  # index+1이 아닌 index부터 시작
#             dfs(elements + [arr[i]], i)

#     dfs([], 0)  # dfs 시작 시, index는 -1이 아니라 0부터 시작

#     return cases

print(combinations([1, 2, 3], 2))

# print(combination_with_replacement([1, 2, 3, 4], 3))