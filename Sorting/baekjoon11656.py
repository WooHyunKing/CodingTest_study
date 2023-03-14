word = input()

data = [0]*(len(word))

for i in range(len(word)):
    data[i] = word[i:]

data.sort()

for i in data:
    print(i)