n = int(input())

solution = 0

weight_list = []

for i in range(n):
  weight_list.append(int(input()))

weight_list.sort()
list_len = len(weight_list)

for i in range(list_len):
  temp = (list_len-i)*weight_list[i]
  if temp > solution:
    solution = temp

print(solution)