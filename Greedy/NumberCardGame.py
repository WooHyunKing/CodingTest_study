# import time
# from tracemalloc import start

# n, m = map(int,input().split())

# result = 0

# for i in range(n):
#     data = list(map(int,input().split()))
#     temp = min(data)
#     if temp>result:
#         result=temp


# print(result)

n, m = map(int,input().split())

result = 0

for i in range(n):
    result = max(result, min(list(map(int,input().split()))))

print(result)



