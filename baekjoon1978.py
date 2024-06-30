import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))

# '1과 자기 자신 외의 약수를 가지지 않는 1보다 큰 자연수

count = 0

def checkPrime(N):

    prime_set = set(range(2,N+1))

    for i in range(2,N+1):
        if i in prime_set:
            prime_set -= set(range(2*i,N+1,i))

    if N in prime_set:
        return True
    else:
        return False


for num in numbers:
    if checkPrime(num):
        count += 1

print(count)