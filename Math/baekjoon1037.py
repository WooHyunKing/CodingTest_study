count = int(input())
real_measure = list(map(int,input().split()))

real_measure.sort()

print(real_measure[0] * real_measure[-1])