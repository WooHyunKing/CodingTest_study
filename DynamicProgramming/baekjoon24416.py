n = int(input())

dp = [0]*41
count = 0

def fib_dynamic(n):
  global count
  
  if n == 1 or n == 2:
    return 1

  if dp[n] != 0:
    return dp[n]

  count += 1
  dp[n] = fib_dynamic(n-1) + fib_dynamic(n-2)

  return dp[n]

print(fib_dynamic(n),count)