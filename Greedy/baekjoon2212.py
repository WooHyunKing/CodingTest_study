import sys
import heapq

input = sys.stdin.readline

# 고속도로 위에 N개의 센서를 설치
# 고속도로 위에 최대 K개의 집중국을 세울 수 있다

# 각 집중국은 센서의 수신 가능 영역을 조절할 수 있다
# 집중국의 수신 가능 영역은 고속도로 상에서 연결된 구간으로 나타나게 된다

# N개의 센서는 적어도 하나의 집중국과는 통신이 가능해야함
# 각 집중국의 '수신 가능 영역의 길이의 합'을 최소화

# 고속도로는 평면상의 직선이라고 가정
# 센서들은 이 직선 위의 한 기점인 원점으로부터의 정수 거리의 위치에 놓여 있다
# 따라서, 각 센서의 좌표는 정수 하나로 표현

# 단, 집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다.

# 출력 : 각 집중국의 수신 가능영역의 거리의 합의 최솟값

N = int(input())
K = int(input())

sensors = sorted(list(set(map(int,input().split()))))
diffs = []

for i in range(len(sensors)-1):
    heapq.heappush(diffs,-abs(sensors[i+1]-sensors[i]))

for _ in range(K-1):

    if diffs:
        heapq.heappop(diffs)

diffs = [-x for x in diffs]

print(sum(diffs))