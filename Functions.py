def Fictorials (n):
    if n == 1 :
        return 1
    else:
        return n * Fictorials(n-1)
print(Fictorials(2) )

def fib (n):
    if n >= 3 :
        return (n-2) + Fictorials(n - 1)
    else:
        return 1
print(fib(5) )