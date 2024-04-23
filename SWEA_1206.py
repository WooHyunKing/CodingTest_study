for index in range(10):
    
    n = int(input())

    heights = list(map(int,input().split()))

    answer = 0

    for i in range(2,n-2):
        temp = heights[i-2:i+3]

        if max(temp) != heights[i]:
            continue
        
        temp.sort()

        answer += abs(temp[-1]-temp[-2])

    print(f"#{index+1} {answer}")