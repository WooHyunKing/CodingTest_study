from collections import deque
import itertools

def calculate_distance(r1,c1,r2,c2):
    return abs(r1-r2) + abs(c1-c2)

n, m = map(int,input().split())

input_city = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

chicken_house_list = set()
house_list = set()

min_value = float("inf")

for i in range(n):
    for j in range(n):
        if input_city[i][j] == 2:
            chicken_house_list.add((i,j))
        elif input_city[i][j] == 1:
            house_list.add((i,j))

combination_list = set(itertools.combinations(chicken_house_list,m))

for combination in combination_list:
    distance = [float("inf") for _ in range(len(house_list))]
    for i, value in enumerate(house_list):
        hx, hy = value[0], value[1]
        for cx, cy in combination:
            distance[i] = min(distance[i], calculate_distance(hx,hy,cx,cy))
    if min_value > sum(distance):
        min_value = sum(distance)

print(min_value)