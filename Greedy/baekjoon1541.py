expression = input()

# '-'를 기준으로 분할 
# ex) ['00009','00009+00008']
split_exp = expression.split('-')

for i in range(len(split_exp)):
  # 분할된 문자열들을 순서대로 '+'를 기준으로 분할 후 합을 구하기(내부는 +로만 이루어져 있기 때문)
  # 그리고 동시에 앞에 0으로 채워진 문자열들을 정수화 시킨다
  # ex) [9, 17]
  split_plus = list(map(int,split_exp[i].split('+')))
  split_exp[i] = sum(split_plus)

# 첫 번째 원소를 제외한 나머지 원소들은 '-'를 기준으로 파싱되었기 때문에 모두 빼주면 된다.
# ex) 9 - 17
print(split_exp[0] - sum(split_exp[1:]))