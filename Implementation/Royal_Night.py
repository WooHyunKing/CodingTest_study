location = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

input = list(input())

count = 0

# 수평 2 수직 1 (왼 2 위 1)

if (location[input[0]] > 2) and (int(input[1]) > 1):
    count += 1

# 수평 2 수직 1 (왼 2 아래 1)
if (location[input[0]] > 2) and (int(input[1]) < 8):
    count += 1

# 수평 2 수직 1 (오 2 위 1)
if (location[input[0]] < 7) and (int(input[1]) > 1):
    count += 1

# 수평 2 수직 1 (오 2 아래 1)
if (location[input[0]] < 7) and (int(input[1]) < 8):
    count += 1

# 수직 2 수평 1 (위 2 왼 1)
if (int(input[1]) > 2) and (location[input[0]] > 1)  :
    count += 1

# 수직 2 수평 1 (위 2 오 1)
if (int(input[1]) > 2) and (location[input[0]] < 8)  :
    count += 1

# 수직 2 수평 1 (아래 2 왼 1)
if (int(input[1]) < 7) and (location[input[0]] > 1)  :
    count += 1

# 수직 2 수평 1 (아래 2 오 1)
if (int(input[1]) < 7) and (location[input[0]] < 8)  :
    count += 1

print(count)