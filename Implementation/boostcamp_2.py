data = list(input().split())

result = ""

def getByte(str):
    if str == "BOOL":
        return 1
    elif str == "SHORT":
        return 2
    elif str == "FLOAT":
        return 4
    elif str == "INT":
        return 8
    elif str == "LONG":
        return 16

for i in range(len(data)):
    if i == 0:
        if data[i] == "BOOL":
            result += "#"
        elif data[i] == "SHORT":
            result += "##"
        elif data[i] == "FLOAT":
            result += "####"
        elif data[i] == "INT":
            result += "########"
        elif data[i] == "LONG":
            result += "################"

    else:
       remain = 8 - (len(result)%8)
       
       if remain < (getByte(data[i])%8):
           result += "."*remain
           result += "#"*getByte(data[i])
       else:
           result += "#"*getByte(data[i])

print(result)
       
        

# print(result)

