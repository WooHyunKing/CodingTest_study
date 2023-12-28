t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int,input().split()))

    answer = 0
    
    # stock = 0
    
    # for i,price in enumerate(prices):
    #     maximum = max(prices[i:])

    #     if maximum == price:
    #         answer += (price*stock)
    #         stock = 0
        
    #     elif price < maximum:
    #         answer -= price
    #         stock += 1

    maximum = prices[-1]

    for i in range(n-2,-1,-1):
        if prices[i] > maximum:
            maximum = prices[i]
        elif prices[i] < maximum:
            answer += (maximum - prices[i])
    
    print(answer)
        
