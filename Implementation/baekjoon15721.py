# 뻔 - 데기 - 뻔 - 데기 - 뻔 - 뻔 - 데기 - 데기
# 뻔 - 데기 - 뻔 - 데기 (고정) + (뻔 x n) - (데기 x n)

a = int(input()) # a <= 2000

t = int(input()) # <= 10000

value = int(input()) # 뻔이면 0, 데기면 1

init = [0,1,0,1,0,0,1,1]

for i in range(2,5001):
    init += [0,1,0,1]
    init += [0]*(i+1)
    init += [1]*(i+1)

current = [0,0]

for index,v in enumerate(init):
    current[v] += 1

    if current[value] == t:
        print(index%a)
        break


# current = [0, 0]
# index = 0

# bun, dae = 0, 0

# while True:
#     if current[value] == t:
#         print(index)
#         break

#     if bun == 2 and dae == 2:
        
    
#     index += 1
    
    

