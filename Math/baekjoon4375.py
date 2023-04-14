# while True:

#     input_data = int(input())

#     mul = 1

#     while True:
#         n = input_data * mul
#         length = len(str(n))

#         is_only_one = False

#         for i in range(length):

#             if n % 10 != 1 :
#                 break

#             if (i == length-1) and n%10 == 1:
#                 is_only_one = True
#                 break

#             n = n // 10
        
#         if is_only_one:
#             print(length)
#             break
        
#         mul += 1


while True: # 무한 입력

    try: #무한 입력이기 때문에 파일의 끝 에러 EOF에러를 잡아주기 위한 try,catch 구문 작성
        n = int(input())

        num = 0
        square = 0

        while True:
            
            num += (10**square)
            
            if num % n == 0 :
                print(square+1)
                break

            square += 1
    
    except EOFError: #파일의 끝에러 EOFError를 처리
        break