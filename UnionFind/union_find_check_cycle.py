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

cycle = False

for i in range(e):
    a, b = map(int,input().split())

    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 Union수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")