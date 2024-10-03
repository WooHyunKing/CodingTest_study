import sys
import heapq

input = sys.stdin.readline

# 국회의원 선거를 조작
# 다솜이의 기계는 각 사람들이 누구를 찍을 지 미리 읽을 수 있다. 
# 어떤 사람이 누구를 찍을 지 정했으면, 반드시 선거때 그 사람을 찍는다.

# 형택구에 나온 국회의원 후보는 N명
# 다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.

# 다솜이는 기호 1번
# 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선이 되게 하려고 한다.
# 다른 모든 사람의 득표수 보다 많은 득표수를 가질 때, 그 사람이 국회의원에 당선

# 출력 : 다솜이가 매수해야하는 사람의 최솟값

N = int(input())

my_vote = int(input())

if N == 1:
    print(0)
    exit()

hq = []

answer = 0

for _ in range(N-1):
    heapq.heappush(hq,-int(input()))

while my_vote <= -hq[0]:
    
    maximum_vote = -heapq.heappop(hq)
    my_vote += 1
    heapq.heappush(hq,-(maximum_vote-1))
    answer += 1


print(answer)