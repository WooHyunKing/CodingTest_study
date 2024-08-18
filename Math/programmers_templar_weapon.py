def solution(number, limit, power):
    answer = 0
    
    # 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매
    # 단, 이웃나라와의 협약에 의해 공격력의 제한수치를 정하고, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매
    
    def count(n):
        
        count = 0
        
        for i in range(1,int(n**(1/2))+1):
            if n%i == 0:
                count += 1
                if i**2 != n:
                    count+=1
    
        return count
    
    for i in range(1,number+1):
        
        result = count(i)
        
        if result <= limit:
            answer += result
        else:
            answer += power
    
    return answer