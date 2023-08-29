t = int(input())

answer = []

for _ in range(t):
    red_set, blue_set = set(), set()

    n = int(input())
    
    for _ in range(n):
        start_x, start_y, end_x, end_y, color =  map(int,input().split())

        for i in range(start_x,end_x+1):
            for j in range(start_y,end_y+1):
                if color == 1:
                    red_set.add((i,j))
                elif color == 2:
                    blue_set.add((i,j))

    answer.append(len(red_set & blue_set))


for i, value in enumerate(answer):
    print(f"#{i+1} value")