import sys
input = sys.stdin.readline

n = int(input())

count_array = [0]*(10001)

for i in range(n):
  data = int(input())
  count_array[data] += 1

for i in range(len(count_array)):
  for j in range(count_array[i]):
    sys.stdout.write(str(i)+'\n')