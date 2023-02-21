import sys
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
  age, name = list(input().split())
  array.append((int(age),name,i))

array.sort(key=lambda x:x[2])
array.sort(key=lambda x:x[0])

for i in range(n):
  print(f"{array[i][0]} {array[i][1]}")