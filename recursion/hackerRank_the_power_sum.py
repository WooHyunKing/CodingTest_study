def powerSum(X, N):
    # Write your code here
    def helper(target,power,num):
        if target == 0:
            return 1
        if target < 0 or num > math.sqrt(target):
            return 0
        # 현재 수를 포함하는 경우와 포함하지 않는 경우의 수를 재귀적으로 계산
        include = helper(target-num**power,power,num+1)
        exclude = helper(target,power,num+1)
        
        return include + exclude
    
    return helper(X,N,1)