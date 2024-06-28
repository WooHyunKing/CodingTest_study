import sys

input = sys.stdin.readline

# DNA 문자열은 모든 문자열에 등장하는 문자가 {‘A’, ‘C’, ‘G’, ‘T’} 인 문자열

# 임의의 DNA 문자열을 만들고 만들어진 DNA 문자열의 부분문자열을 비밀번호로 사용
# 부분문자열에서 등장하는 문자의 개수가 특정 개수 이상이여야 비밀번호로 사용할 수 있다

# 단, 부분문자열이 등장하는 위치가 다르다면 부분문자열이 같다고 하더라도 다른 문자열로 취급한다.

s_length, p_length = map(int,input().split())

string = input().rstrip()

a, c, g, t = map(int,input().split())

dictionary = dict()

answer = 0

dictionary['A'], dictionary['C'], dictionary['G'], dictionary['T'] = 0, 0, 0, 0 

for i in range(p_length):
    dictionary[string[i]] += 1

if dictionary['A'] >= a and dictionary['C'] >= c and dictionary['G'] >= g and dictionary['T'] >= t:
    answer += 1

for i in range(p_length,s_length):
    dictionary[string[i-p_length]] -= 1
    dictionary[string[i]] += 1

    if dictionary['A'] >= a and dictionary['C'] >= c and dictionary['G'] >= g and dictionary['T'] >= t:
        answer += 1

print(answer)