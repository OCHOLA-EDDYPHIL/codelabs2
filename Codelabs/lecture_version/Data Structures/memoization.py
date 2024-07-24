def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



memo = {}
def fib(n):
    if n in memo: return memo[n] 
    if n == 0:
        memo[0] = 0
        return 0
    if n==1:
        memo[1] = 1
        return 1
    val = fib(n-1) + fib(n-2)
    memo[n] = val
    return val

# print(fib(100))
print(memo)
print(fib(50))
