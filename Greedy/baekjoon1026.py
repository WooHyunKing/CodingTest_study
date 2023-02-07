n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()

a_resort = [0] * n
b_index = []

for i in range(n):
    b_index.append((i,b[i]))

b_index.sort(key=lambda x:-x[1])

for i in range(n):
    a_resort[b_index[i][0]] = a[i] 

sum = 0

for i in range(n):
    sum += (a_resort[i] * b[i])

print(sum)
