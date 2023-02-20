# n = int(input())

# array=[]

# for i in range(n):
#     array.append(int(input()))

# array.sort(reverse=True)

# for i in array:
#     print(i,end=' ')

n = int(input())

arr = [0]*n

for i in range(n):
    arr[i] = int(input())

arr.sort(reverse=True)

for i in range(n):
    print(arr[i],end=' ')