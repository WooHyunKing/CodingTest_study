import copy

l, c = map(int,input().split())

alpha_set = set(input().split())

answer = []

vowels = set(['a','e','i','o','u'])

# 암호는 서로 다른 L개의 알파벳 소문자들로 구성
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것

def dfs(string,remain_set):
    
    if len(string) == l: # 알파벳 개수가 L개인 경우 종료
        vowel_count = len([x for x in string if x in vowels]) # 모음 개수
        consonant_count = len(string) - vowel_count # 자음 개수

        if vowel_count >= 1 and consonant_count >= 2: # 조건에 부합하는 경우 answer에 추가
            answer.append("".join(string))

        return

    for item in remain_set: # 나머지 문자들을 탐색
        if len(string) == 0: # 첫번째 원소인 경우에는 그냥 추가
            new_set = copy.deepcopy(remain_set)
            new_set.discard(item)
            dfs(string+[item], new_set)
        else: # 나머지의 경우 증가하는 순서를 유지하면서 추가
            if item > string[-1]:
                new_set = copy.deepcopy(remain_set)
                new_set.discard(item)
                dfs(string+[item],new_set)

dfs([],alpha_set)

for ans in sorted(answer):
    print(ans)