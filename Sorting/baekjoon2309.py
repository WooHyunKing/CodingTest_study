from itertools import combinations

array = [0]*9

for i in range(9):
  array[i] = int(input())

remain = sum(array)-100

com_list = list(combinations(array,2))

for i in com_list:
  if sum(i) == remain:
    array.remove(i[0])
    array.remove(i[1])
    break

array.sort()

for i in array:
  print(i)