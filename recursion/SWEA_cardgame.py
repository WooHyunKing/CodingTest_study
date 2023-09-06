t = int(input())

def who_win(a,b):
    if cards[a] == cards[b]:
        return min(a,b)
    
    elif cards[a] == 1:
        if cards[b] == 2:
            return b
        elif cards[b] == 3:
            return a
    elif cards[a] == 2:
        if cards[b] == 1:
            return a
        elif cards[b] == 3:
            return b
    elif cards[a] == 3:
        if cards[b] == 1:
            return b
        elif cards[b] == 2:
            return a

def grouping(start,end):
    if start == end:
        return start
    
    front = grouping(start,(start+end)//2)
    back = grouping((start+end)//2+1,end)

    return who_win(front,back)

for i in range(t):
    n = int(input())

    cards = list(map(int,input().split()))
    
    print(f"#{i+1} {grouping(0,len(cards)-1) + 1}" )