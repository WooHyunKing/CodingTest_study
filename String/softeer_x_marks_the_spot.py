import sys

# 1. n개의 문자열쌍(S,T)이 주어지는데, 각 쌍에 대해서 S와 T의 길이는 같다
# 2. S에서 글자 x 또는 X가 등장하는 위치를 P라고 한다.(유일)
# 3. 이때 T의 P번째 글자를 읽는다.(소문자는 대문자로 변환)

input = sys.stdin.readline

N = int(input())

answer = []

for _ in range(N):
    str1, str2 = input().split()

    str1_set, str2_set = set(str1), set(str2)

    x_index = -1
    X_index = -1

    if 'x' in str1_set:
        x_index = str1.find('x')
    elif 'X' in str1_set:
        X_index = str1.find('X')

    if x_index != -1:
        answer.append(str2[x_index].upper())
    else:
        answer.append(str2[X_index].upper())

print("".join(answer))