def solution(N, number):
    answer = -1
    
    if N == number:
        return 1
    
    # N을 i+1번 사용했을 때 만들 수 있는 값들
    dp = [set() for i in range(9)]
    
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
    
    for i in range(2,9):
        for j in range(1,i):
            for term1 in dp[j]:
                for term2 in dp[i-j]:
                    dp[i].add(term1 + term2)
                    dp[i].add(term1 - term2)
                    dp[i].add(term1 * term2)
                    if term2 != 0:
                        dp[i].add(term1 // term2)
        if number in dp[i]:
            return i
                    
    return answer