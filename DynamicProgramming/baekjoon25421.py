n = int(input())

data = [1 for x in range(1,10)]

for i in range(n-1):

    temp = []

    for j in range(9):
        value = 0
        for k in range(j-2,j+3):
            if 0 <= k <= 8:
                value += data[k]
        temp.append(value%987654321)
    
    data = temp

print(sum(data)%987654321)