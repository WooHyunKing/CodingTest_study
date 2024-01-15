import copy

k = int(input())

signs = list(input().split())

minimum, maximum = float("inf"), float("-inf")

def dfs(numbers,num_set):

    global minimum, maximum, minimum_string, maximum_string

    length = len(numbers)
    
    if length == k+1:
        final_value = int("".join(list(map(str,numbers))))
        if final_value < minimum:
            minimum = final_value
            minimum_string = "".join(list(map(str,numbers)))
        if final_value > maximum:
            maximum = final_value
            maximum_string = "".join(list(map(str,numbers)))
        return
    
    for num in num_set:
        
        if length == 0: # 첫번째 원소인 경우
            new_set = copy.deepcopy(num_set)
            new_set.discard(num)
            dfs(numbers+[num],new_set)

        else: # 부등호에 따라 다르게 탐색
            if signs[length-1] == '<' and numbers[length-1] < num:
                new_set = copy.deepcopy(num_set)
                new_set.discard(num)
                dfs(numbers+[num], new_set)
            elif signs[length-1] == '>' and numbers[length-1] > num:
                new_set = copy.deepcopy(num_set)
                new_set.discard(num)
                dfs(numbers+[num], new_set)

dfs([], set([0,1,2,3,4,5,6,7,8,9])) 

print(maximum_string)
print(minimum_string)