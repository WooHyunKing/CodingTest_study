from itertools import combinations
import time

n = int(input())

num_list = list(map(int,input().split()))

# start = time.time()

# num_list = [x for x in range(1,2001)]

answer = float("-inf")

def makeBinaryCount(number):

    binary = []
    
    while number != 0:
        binary.append(number % 2)
        number = number // 2
    
    return list(reversed(binary)).count(1)

combs = list(combinations(num_list,2))

for v1, v2 in combs:
    answer = max(answer,makeBinaryCount(v1+v2))

# end = time.time()

# print(end-start)

print(answer)