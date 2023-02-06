n = int(input())

soluton = 0

# 3의 배수인 경우랑 5의 배수인 경우 거르기
# 3의 배수는 3의 개수를 5로 나눠서 몫 *3  + 나머지
if n%3 == 0:
    soluton = n // 3
    soluton = ((soluton//5)*3) + (soluton%5)

# 5의 배수는 그대로
elif n%5 == 0:
    soluton = n//5

# 5를 먼저 빼고 3으로 나눠지는지 확인
# 3으로 나눠지면 3으로 나눠서 그 몫을 더해주고 끝
# 3으로 나눠지지 않으면 5 한번더 빼기
else:
    while n != 0:

        # n이 1~2 이 되면 답이 X
        if n < 3 and n > 0:
            soluton = -1
            break

        # 5보다 크거나 같은 경우엔 5빼기
        if n >= 5 :
            soluton += 1
            n -= 5
        
        # 3,4인 경우
        elif n>=3:
            soluton += 1
            n -= 3
        
        if n%3 == 0:
            # soluton += n//3
            temp = n//3
            soluton += ((temp//5)*3) + (temp%5)
            n %= 3

print(soluton)



                                




