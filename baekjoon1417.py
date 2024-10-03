import sys
input = sys.stdin.readline

# {1, 2, ..., 49}에서 수 6개를 고른다
# 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것

def combinations(arr, k):

    cases = []

    def dfs(elements,index):
        if len(elements) == k:
            cases.append(elements)
            return
        for i in range(index+1,len(arr)):
            dfs(elements+[arr[i]],i)
    
    dfs([],-1)

    return cases

while True:

    numbers = list(map(int,input().split()))

    if len(numbers) == 1 and numbers[0] == 0:
        break

    k = numbers[0]
    numbers = numbers[1:]

    answer = sorted(combinations(numbers,6))
    
    for a in answer:
        for b in a:
            print(b, end=' ')
        print()
    print()