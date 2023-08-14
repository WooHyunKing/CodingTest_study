n = int(input())

data = list(map(int,input().split()))

data.insert(0,0)

index_list = [0]*(n+1)

count = 1
max_length = -1

for i in range(1,n+1):
    index_list[data[i]] = i

for i in range(1,n):
    if index_list[i] < index_list[i+1]:
        count += 1
        max_length = max(max_length, count)
    else:
        count = 1

if max_length != -1:
    print(n - max_length)
else:
    print(0)