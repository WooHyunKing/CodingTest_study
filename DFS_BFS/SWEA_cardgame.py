t = int(input())

answer = []

def who_win(a,b,cards):
    if cards[a] == 1:
        if cards[b] == 2:
            return b
        elif cards[b] == 3:
            return a
        else:
            a
    elif cards[a] == 2:
        if cards[b] == 1:
            return a
        elif cards[b] == 3:
            return b
        else:
            return a
    elif cards[a] == 3:
        if cards[b] == 1:
            return b
        elif cards[b] == 2:
            return a
        else:
            return a


def divide_and_conquer(cards,n,m):  

    print(n,m)
    print(cards[n],cards[m])

    if abs(n-m) == 1:
        return who_win(n,m,cards)
    
    mid = (n+m)//2

    return who_win(divide_and_conquer(cards,n,mid), divide_and_conquer(cards,mid,m),cards)


for _ in range(t):
    n = int(input())

    cards = list(map(int,input().split()))
    
    print(divide_and_conquer(cards,0,n-1))

# for i,value in enumerate(answer):
#     print(f"#{i+1} {value}")