# ATM

n = int(input())
time_list = list(map(int,input().split()))

time_list.sort()

total = 0
solution = 0

for i in time_list:
    total = total + i
    solution += total

print(solution)