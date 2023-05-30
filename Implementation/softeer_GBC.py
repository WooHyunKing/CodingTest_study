import sys

n,m = map(int,input().split())

limit = [0]*101

index = 1
test_index = 1

max_value = 0

for i in range(n):
    length, limit_fast = map(int,input().split())
    for j in range(index,index+length):
        limit[j] = limit_fast
    index += length
for i in range(m):
    test_length, test_fast = map(int,input().split())
    for j in range(test_index,test_index + test_length):
        if test_fast > limit[j]:
            diff = test_fast-limit[j]
            if diff > max_value:
                max_value = diff
    test_index += test_length

print(max_value)