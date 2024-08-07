# 서로소 집합 자료구조란 ? 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# 서로소 집합 자료구조는 union과 find이 2개의 연산으로 조작할 수 있다.

# Union 연산 : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# Find 연산 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

# 두 집합이 서로소 관계인지 확인할 수 있는 자료구조
# 서로소 집합 자료구조를 구현할 때는 '트리' 자료구조를 사용하여 집합을 표현

#노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int,input().split())

# 부모 테이블 초기화
parent = [0] * (v+1)

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# 특정 원소가 속한 집합(루트 노드)찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        # return find_parent(parent,parent[x]) # 경로 압축 개선 전
        parent[x] = find_parent(parent,parent[x]) # 경로 압축 개선 후(find 함수를 재귀적으로 호출한 뒤 부모 테이블을 갱신하는 기법)
    # return x # 경로 압축 개선 전
    return parent[x] # 경로 압축 개선 후(루트 노드에 빠르게 접근할 수 있다는 점에서 시간복잡도 개선)

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합 : ", end="")
for i in range(1,v+1):
    print(find_parent(parent,i), end=" ")

print()

# 부모 테이블 내용 출력
print("부모 테이블 내용 : ",end="")
for i in range(1,v+1):
    print(parent[i],end=" ")