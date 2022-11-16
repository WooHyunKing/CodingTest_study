n = int(input())

List = []

for i in range(n):
    input_data = input().split()
    List.append((input_data[0], int(input_data[1])))

List.sort(key=lambda x:x[1])

print(List)

for stuent in List:
    print(stuent[0], end=' ')