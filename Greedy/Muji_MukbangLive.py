# from operator import itemgetter

# def solution(food_times, k):
    
#     foods = []
#     n = len(food_times)
    
#     for i in range(n):
#         foods.append((food_times[i],i+1))

#     foods.sort() # 오름차순으로 음식 정보 정렬
    
#     pretime = 0
    
#     for i, food in enumerate(foods):
        
#         diff = food[0] - pretime # 세로(소요시간 차이)
        
#         if diff != 0:
#             spend = diff * n # 세로 x 가로(남은 음식 수), 소요시간
            
#             if spend <= k: # 소요 시간이 남은 시간보다 작거나 같은 경우(먹을 시간이 있는 경우)
#                 k -= spend
#                 pretime = food[0]
#             else: # 소요 시간이 남은 시간보다 많은 경우(시간 부족한 경우)
#                 k %= n
#                 sublist = sorted(foods[i:],key=itemgetter(1))
#                 return sublist[k][1]
        
#         n -= 1
    
#     return -1

from operator import itemgetter

def solution(food_times, k):
    
    foods = []
    food_count = len(food_times) # 가로(남은 음식 개수)
    
    # 튜플 자료형으로 음식의 소요 시간과 인덱스를 저장
    for i in range(food_count):
        foods.append((food_times[i],i+1))
    
    # 튜플 자료형은 첫 번째 원소를 기준으로 정렬 !
    foods.sort()
    
    pretime = 0 
    
    # enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 튜플(tuple)을 만들어줍니다. 따라서 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 인자 풀기(unpacking)를 해줘야 합니다.
    for i,food in enumerate(foods):
        diff = food[0] - pretime # 세로(소요 시간)
        if diff != 0:
            spend = diff*food_count # 총 소요시간(세로 x 가로)

            if spend <= k: # 총 소요시간이 k보다 쟉은 경우
                k -= spend
                pretime = food[0]

            else: # 총 소요시간이 k 보다 오래 걸릴 경우
                k %= food_count # 나머지 계산
                sublist = sorted(foods[i:],key = itemgetter(1)) # 인덱스 기준으로 재정렬
                return sublist[k][1] # 정답 인덱스
            
        food_count -= 1 # 하나의 음식을 모두 섭취했으니 남은 음식 개수 최신화
        
    return -1