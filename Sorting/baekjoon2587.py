import math

array = [0] * 5

for i in range(5):
    array[i] = int(input())

array.sort()

print(math.floor(sum(array)/5))
print(array[2])