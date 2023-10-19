area = [["."]*3 for _ in range(3)]

cases = set()

def check_is_full():
    is_full = True
    
    for i in range(3):
        for j in range(3):
            if area[i][j] == '.':
                is_full = False

    return is_full

def check_tictac():

    if check_is_full():
        return True

    if (area[0][0] == area[0][1] == area[0][2] and area[0][0] != ".") or (area[1][0] == area[1][1] == area[1][2] and area[1][0] != '.') or (area[2][0] == area[2][1] == area[2][2] and area[2][0] != '.') or (area[0][0] == area[1][0] == area[2][0] and area[0][0] != '.') or (area[0][1] == area[1][1] == area[2][1] and area[0][1] != '.') or (area[0][2] == area[1][2] == area[2][2] and area[0][2] != '.') or (area[0][0] == area[1][1] == area[2][2] and area[0][0] !='.') or (area[0][2] == area[1][1] == area[2][0] and area[0][2] != '.') :
        return True
    
    return False


def dfs(current):
    
    if check_tictac():
        temp = ""
        for row in area:
            temp += "".join(row)
        cases.add(temp)
        return
    
    for i in range(3):
        for j in range(3):
            if area[i][j] == '.':
                area[i][j] = current
                if current == "X":
                    dfs("O")
                else:
                    dfs("X")
                area[i][j] = "."

dfs("X")


while True:
    
    string = input()

    if string == 'end':
        break

    if string in cases:
        print("valid")
    else:
        print("invalid")