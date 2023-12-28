# 1. 수의 각 자리 숫자 중에서 홀수의 개수를 종이에 적는다.
# 2. 수가 한자리이면 더 이상 아무것도 하지 못하고 종료
# 3. 수가 두자리이면 2개로 나눠서 합을 구하여 새로운 수로 생각
# 4. 수가 세자리 이상이면 임의의 위치에서 끊어서 3개의 수로 분할 후 3개를 더한 값을 새로운 수로 생각

# 주어진 수 N (<= 10^9)

# 최종값의 '홀수의 개수'의 최솟값과 최댓값 구하기

from itertools import combinations

n = int(input())

minimum = float("inf")
maximum = float("-inf")

def count_odd(arr):
    count = 0
    for i in arr:
        if int(i)%2 == 1:
            count += 1
    return count

def dfs(num_str,odd_count):

    global minimum
    global maximum

    current_odd_count = count_odd(num_str)
    
    if len(num_str) == 1:
        new_count = odd_count + current_odd_count
        if new_count < minimum:
            minimum = new_count
        if new_count > maximum:
            maximum = new_count
        return

    elif len(num_str) == 2:
        new_num = int(num_str[0]) + int(num_str[1])
        new_str = list(str(new_num))

        dfs(new_str, odd_count + current_odd_count)
        # joined = "".join(num_str)

    elif len(num_str) >= 3:
        index_list = [x for x in range(1,len(num_str))]

        combs = list(combinations(index_list,2))

        for first, second in combs:
            one = "".join(num_str[:first])
            two = "".join(num_str[first:second])
            three = "".join(num_str[second:])

            total = list(str(int(one) + int(two) + int(three)))
            
            dfs(total,odd_count+current_odd_count)

dfs(list(str(n)),0)

print(f"{minimum} {maximum}")
