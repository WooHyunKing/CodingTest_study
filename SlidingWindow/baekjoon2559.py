import sys

input = sys.stdin.readline

n, k = map(int,input().split())

temp_list = list(map(int,input().split()))

value = sum(temp_list[:k])

answer = value

for i in range(k,n):
    
    value -= temp_list[i-k]
    value += temp_list[i]

    answer = max(answer,value)

print(answer)