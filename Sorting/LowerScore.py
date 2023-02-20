# n = int(input())

# List = []

# for i in range(n):
#     input_data = input().split()
#     List.append((input_data[0], int(input_data[1])))

# List.sort(key=lambda x:x[1])

# # print(List)

# for stuent in List:
#     print(stuent[0], end=' ')

n = int(input())

arr = []

for i in range(n):
    data = tuple(input().split())
    arr.append(data)

arr.sort(key=lambda x:x[1])

for i in arr:
    print(i[0],end=' ')