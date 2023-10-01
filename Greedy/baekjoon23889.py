from itertools import combinations

n,m,k = map(int,input().split())

# i번째 마을의 모래성의 개수 xi
house_count = [0]+list(map(int,input().split()))

# 돌이 굴러가기 시작하는 마을의 위치
rock_locations = list(map(int,input().split()))

house_status = [True]*(n+1)

# 벽의 개수 m개의 줄에 걸쳐 가장 많은 모래성을 지키기 위하여 
# 벽을 설치해야 할 마을의 위치를 오름차순으로 출력
# (2가지 이상의 경우에는 사전순으로 가장 빠른 답을 출력)

for rock in rock_locations:
    house_status[rock] = False

cases = []

for start in rock_locations:
    total = house_count[start]
    for i in range(start+1,n+1):
        if not house_status[i]:
            break
        total += house_count[i]
    cases.append((total,start))

cases.sort(key=lambda x:(x[0],-x[1]))

answer = sorted([x[1] for x in cases[-m:]])

for i in answer:
    print(i)