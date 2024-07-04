import sys

input = sys.stdin.readline

from collections import deque

# 강을 가로지르는 하나의 차선으로 된 다리
# 이 다리를 n 개의 트럭이 건너가려고 한다
# 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다.

# 다리 위에는 단지 w 대의 트럭만 동시에 올라갈 수 있다. 

# 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정

# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.

# 참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정

# n - 다리를 건너는 트럭의 수 / w - 다리의 길이 / L - 다리의 최대하중
n, w, l = map(int,input().split())

weights = list(map(int,input().split()))

weights = deque([(x,w) for x in weights])

area = deque([])

time, current_weight = 0, 0

available = l

while True:
    
    if current_weight == 0 and len(weights) <= 0 and len(area) <= 0:
        break

    if area and area[0][1] <= 0:
        current_weight -= area[0][0]
        area.popleft()
        available += 1

    if weights and available > 0 and weights[0][0] + current_weight <= l:
        current_weight += weights[0][0]
        area.append(weights[0])
        weights.popleft()
        available -= 1
    
    for i in range(len(area)):
        area[i] = (area[i][0], area[i][1]-1)

    time += 1

    # print("weights : ",weights)
    # print("area : ",area)
    # print("current_weight", current_weight)
    # print("time : ",time)
    # print()

print(time)