n = int(input())

data = list(map(int,input().split()))
answer = [0]*n
visited = [False]*n

for i,value in enumerate(data):

    print(answer)
    print(visited)

    index = 1

    # if visited[index]:
    #     index += 1
    
    while value > 0:

        while visited[index]:
            index += 1

        value -= 1
     
        # if visited[index]:
        #     index += 1

        # else:  
        #     value -= 1
        #     index += 1
            # if i != 0:
            #     value -= 1
            #     index += 1
            # else:
            #     index += 1
    
    answer[index] = i+1
    visited[index] = True

print(answer)
    