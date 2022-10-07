from operator import itemgetter

def solution(food_times, k):
    
    foods = []
    n = len(food_times)
    
    for i in range(n):
        foods.append((food_times[i],i+1))

    foods.sort() # 오름차순으로 음식 정보 정렬
    
    pretime = 0
    
    for i, food in enumerate(foods):
        
        diff = food[0] - pretime # 세로(소요시간 차이)
        
        if diff != 0:
            spend = diff * n # 세로 x 가로(남은 음식 수), 소요시간
            
            if spend <= k: # 소요 시간이 남은 시간보다 작거나 같은 경우(먹을 시간이 있는 경우)
                k -= spend
                pretime = food[0]
            else: # 소요 시간이 남은 시간보다 많은 경우(시간 부족한 경우)
                k %= n
                sublist = sorted(foods[i:],key=itemgetter(1))
                return sublist[k][1]
        
        n -= 1
    
    return -1