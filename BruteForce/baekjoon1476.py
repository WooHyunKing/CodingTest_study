E, S, M = map(int,input().split())

RESULT_RANGE = 15*28*19 + 1

for i in range(RESULT_RANGE):

    a, b, c = i%15 + 1, i%28 + 1, i%19 + 1

    if E == a and S == b and M == c:
        print(i + 1)
        break

    
#1 -> 1
#2 -> 2
#3 -> 3
# ..
# 15 -> 15
# 16 -> 1
# 17 -> 2
# 30 -> 15