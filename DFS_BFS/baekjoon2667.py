n = int(input())

# 2차원 배열 지도
arr = []
# 방문 여부 확인용 2차원 배열
visited =[[False]*n for _ in range(n)]
# 단지 내 가구 수
count = 0
# 단지 내 가구 수 리스트
count_list = []

for i in range(n):
  arr.append(list(map(int,list(input()))))

# dfs 함수
def dfs(x,y):
  global count
  # 집이 존재한지 / 방문한 적 있는지 여부 확인
  if arr[x][y] == 1 and not visited[x][y]:
    # 방문 처리
    visited[x][y] = True
    # 단지 내 가구 수 증가
    count += 1

    # 상-하-좌-우로 이동하기 위한 값
    nx = [-1,1,0,0]
    ny = [0,0,-1,1]
    
    for i in range(4):
      # 상-하-좌-우 인덱스 설정
      temp_x = x+nx[i]
      temp_y = y+ny[i]

      # 배열 범위를 벗어나는지 여부 확인
      if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < n:
        # 다음 위치가 집이 존재하는지 / 방문한 적 있는지 여부 확인
        if arr[temp_x][temp_y] == 1 and not visited[temp_x][temp_y]:
          # 집이 존재하고, 방문한 적이 없으면 방문(dfs 재귀)
          dfs(temp_x,temp_y)
    return True
  # 집이 존재하지 않거나 방문한 적 있다면 PASS
  else :
    return False
  
# 모든 위치에 관하여 반복문으로 돌면서 dfs 처리
for i in range(n):
  for j in range(n):
    if dfs(i,j): # 만약에 True를 반환하면 하나의 단지가 만들어지고, count를 초기화(새로운 단지 내 가구수를 찾기 위해)
      count_list.append(count)
      count = 0

# 단지 개수 출력
print(len(count_list))

# 단지 내 가구수 오름차순 정렬
count_list.sort()

# 단지 내 가구수 차례대로 출력
for i in range(len(count_list)):
  print(count_list[i])