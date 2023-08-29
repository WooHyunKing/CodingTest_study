from itertools import combinations
t = int(input())

answer = []
set_a = [i for i in range(1,13)]

for _ in range(t):
    total = 0

    n, k = map(int,input().split())
    subset = list(combinations(set_a,n))
    
    for i in subset:
        if sum(i) == k:
            total += 1
    
    answer.append(total)

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")