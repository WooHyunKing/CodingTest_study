input_str = list(input())

result = []
sum = 0

for i in range(len(input_str)):
    if (input_str[i] >= 'A') and (input_str[i]<='Z'):
        result.append(input_str[i])
    else:
        sum += int(input_str[i])

result.sort()
result = ''.join(result)

print(result+str(sum))

