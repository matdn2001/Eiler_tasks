def Fib(n):
    if n == 1 or n == 2:
        return n
    else:
        return Fib(n - 2) + Fib(n - 1)

a = 2
s = 0
while Fib(a) < 4000000:
    if Fib(a) % 2 == 0:
        s += Fib(a)
    a += 1
print(s)