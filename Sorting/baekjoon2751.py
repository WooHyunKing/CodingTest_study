n = int(input())

array = [0]*n

for i in range(n):
  array[i] = int(input())

array.sort()

for i in array:
  print(i)