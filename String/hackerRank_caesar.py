def caesarCipher(s, k):
    # Write your code here
    length = len(s)
    str_list = list(s)
    k %= 26
    
    for i in range(length):
        char_ord = ord(str_list[i])
        
        if char_ord >= ord('A') and char_ord <= ord('Z'):
            if char_ord + k > ord('Z'):
                diff = ord('Z') - char_ord
                index = (ord('A')-1) + (k-diff)
                str_list[i] = chr(index)
            else:
                str_list[i] = chr(char_ord+k)
        
        elif char_ord >= ord('a') and char_ord <= ord('z'):
            if (char_ord+k) > ord('z'):
                diff = ord('z') - char_ord
                index = (ord('a')-1) + (k-diff)
                str_list[i] = chr(index)
            else:
                str_list[i] = chr(char_ord+k)
    
    return ''.join(str_list)