s = input()

str_length = len(s)

length_list=[]

for length in range(1,str_length+1):

    temp_length = str_length

    result = [s[j:j+length] for j in range(0,len(s),length)]

    # print(result)

    count = 1

    for i in range(len(result)):
        
        if i == (len(result)-1) :
            if count>1:
                temp_length -= (length * count)
                temp_length += (length + len(str(count)))
                count = 1
            break
            
        if result[i] == result[i+1]: # 다음 문자열과 동일한 경우
            count+=1
        elif count>1: # 동일하지 않은 경우
            temp_length -= (length * count)
            temp_length += (length + len(str(count)))
            count = 1
    # print("length is ", length)
    # print(temp_length)
    # print("")
    length_list.append(temp_length)


print(min(length_list))
# length * 반복 횟수 => length + 1