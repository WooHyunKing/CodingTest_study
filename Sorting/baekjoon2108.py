import sys
input = sys.stdin.readline

# n 입력받기
n = int(input())

# n개의 값을 저장하는 리스트
array = [0]*n
# 빈도수를 저장하는 리스트
count_list = []

# 최빈값
mode = 0

# 입력받기
for i in range(n):
  array[i] = int(input())

# 중간 인덱스
mid_index = n//2

# 오름차순 정렬
array.sort()

# 집합 자료형 사용
set_n = set(array)
# 사전 자료형 사용
dictionary = dict()

# 사전 자료형에 숫자 '값 : 빈도수(카운팅)' 저장 => 시간복잡도 최소화
for i in array:
  if i not in dictionary:
    dictionary[i] = 1
  else:
    dictionary[i] += 1

# 빈도수 리스트에 튜플(값, 빈도수)로 저장
for i in set_n:
  count_list.append((i, dictionary[i]))

# 먼저 값의 내림차순으로 정렬(추후에 2번째로 작은 값을 구하기 위해)
count_list.sort(key=lambda x:-x[0])
# 빈도수를 기준으로 오름차순 정렬(최빈값을 찾기위해)
count_list.sort(key=lambda x:x[1])

count_c = len(count_list)

# 최빈 값이 같은 것이 여러 개 경우에 2번째로 작은 값을 최빈값으로 설정
if count_list[count_c-1][1] == count_list[count_c-2][1]:
  mode = count_list[count_c-2][0]
# 최빈 값이 유일한 경우엔 그대로 반환
else:
  mode = count_list[count_c-1][0]

print(round(sum(array)/n)) # 산술평균
print(array[mid_index]) # 중앙값
print(mode) # 최빈값
print(array[n-1]-array[0]) # 범위