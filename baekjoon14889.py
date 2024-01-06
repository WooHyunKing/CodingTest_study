from itertools import combinations
from itertools import permutations

n = int(input())

member = set([x for x in range(n)])

answer = float("inf")

area = [list(map(int,input().split())) for _ in range(n)]

case_list = list(combinations([x for x in range(n)], n//2))
case_list = case_list[:len(case_list)//2]

def calculate(numbers):
    cases = permutations(numbers,2)
    return sum([area[x][y] for x,y in cases])

for team_a in case_list:
    team_b = [x for x in range(n) if x not in team_a]
    diff = abs(calculate(team_a)-calculate(team_b))

    if diff < answer:
        answer = diff

print(answer)