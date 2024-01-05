def solution(s):
    words = s.split()
    blanks = []
    
    for i,value in enumerate(s):
        if value == ' ': # 공백문자인 경우
            if i == 0: # 첫번째 문자인 경우(index error 방지)
                blanks.append(' ')
            else:
                if s[i-1] == ' ': # 연속된 공백문자일 경우
                    blanks[-1] += ' '
                else:
                    blanks.append(' ')
    
    def convertWord(string): # JadenCase로 문자열 변환해주는 함수
        result = ''
        for i,value in enumerate(string):
            if i == 0:
                if ord('a') <= ord(value) <= ord('z'):
                    result += chr(ord(value)-32)
                else:
                    result += value
            else:
                if ord('A') <= ord(value) <= ord('Z'):
                    result += chr(ord(value)+32)
                else:
                    result += value
        return result
    
    def startWithBlank(wordList, blankList):
        result = []
        
        for i in range(len(wordList)):
            result.append(blankList[i])
            result.append(wordList[i])
        
        return result
    
    def endWithBlank(wordList, blankList):
        result = []
        
        for i in range(len(wordList)):
            result.append(wordList[i])
            result.append(blankList[i])
        
        return result
    
    def blankInTheMiddle(wordList, blankList):
        result = []
        for i in range(len(blankList)):
            result.append(wordList[i])
            result.append(blankList[i])
        return result + [wordList[-1]]
    
    def blankOnBothSide(wordList, blankList):
        result = []
        for i in range(len(wordList)):
            result.append(blankList[i])
            result.append(wordList[i])
        return result + [' ']
    
    words = [convertWord(x) for x in words]
    
    if len(words) == len(blanks): # (단어 개수 == 빈칸 개수)
        if s[0] == ' ': # ' ' A ' ' B
            return "".join(startWithBlank(words,blanks))
        else: # A ' ' B ' '
            return "".join(endWithBlank(words,blanks))
    elif len(words) == (len(blanks) + 1): # A ' ' B (단어 개수 == 빈칸 개수 + 1)
        return "".join(blankInTheMiddle(words,blanks))
    elif len(words) == (len(blanks) - 1): # ' ' A ' ' B ' ' (단어 개수 == 빈칸 개수 - 1)
        return "".join(blankOnBothSide(words,blanks))