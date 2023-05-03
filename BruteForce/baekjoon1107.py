n = int(input())
m = int(input())
ans = abs(100 - n)

if m != 0: # 고장난게 있을 경우만 인풋을 받음
    broken = list(input().split())
else:
    broken = []

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for i in range(1000001):
    for j in str(i):
        if j in broken: #해당 숫자 버튼이 고장난 경우 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
        ans = min(ans, len(str(i)) + abs(i - n)) #min(기존답, 숫자 버튼 클릭 수 + 해당 번호로부터 타겟까지의 차이)

print(ans)

# # 자리수의 차를 구하는 함수
# def find_diff(number,set):

#     upper_bool = False
#     lower_bool = False

#     upper = 0
#     lower = 0
    
#     for i in range(number,10):
#         if i in set:
#             upper_bool = True
#             upper = abs(i-number)
#             break

#     for i in range(number,-1,-1):
#         if i in set:
#             lower_bool =True
#             lower = abs(i-number)
#             break

#     if upper_bool and lower_bool:
#         return min(upper,lower)
#     elif upper_bool:
#         return upper
#     elif lower_bool:
#         return lower

# n = int(input())
# m = int(input())

# NUMBER_OF_DIGITS = len(str(n))
# NUMBER_N = int(n)

# number_set = {}

# count = 0

# if m > 0 :
#     wrong_number_set = set(map(int,input().split()))
#     number_set = {0,1,2,3,4,5,6,7,8,9} - wrong_number_set

# if (abs(n-100) <= NUMBER_OF_DIGITS):
#     print(abs(n-100))

# elif m == 0:
#     print(NUMBER_OF_DIGITS)

# else:
#     # for i in range(NUMBER_OF_DIGITS):
#     #     count += (find_diff(int(n[i]),number_set) * 
#     max_set_value = max(number_set)
    

#     mul = 1
#     while(mul <= ( 10 ** (NUMBER_OF_DIGITS -1))):
#         compare_value = 0
#         compare_mul = 1 

#         while (len(str(compare_mul)) < len(str(mul))):
#             compare_value += max_set_value * compare_mul
#             compare_mul *= 10
#             print(compare_value)

#         count += 1
#         print(f"one : {abs(mul-compare_value)}")
#         print(f"two : {find_diff(NUMBER_N%10,number_set) * mul}") 
#         if find_diff(NUMBER_N%10,number_set) != 0:
#             count += min(abs(mul-compare_value),(find_diff(NUMBER_N%10,number_set) * mul)) 
#         else:
#             count += max(abs(mul-compare_value),(find_diff(NUMBER_N%10,number_set) * mul)) 
#         # count += min(abs(mul-compare_value),(find_diff(NUMBER_N%10,number_set) * mul)) 


#         # if find_diff(NUMBER_N%10,number_set) != 0:
#         #     count += min(abs(n%compare_mul-compare_value),(find_diff(NUMBER_N%10,number_set) * mul)) 
#         # else:
#         #     count += (find_diff(NUMBER_N%10,number_set) * mul)

#         mul *= 10
#         NUMBER_N //= 10
    
#     print(count)


# # 70000
# # 10000 + 5

# # 77777
# # 5 + 2223