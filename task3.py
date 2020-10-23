x = 600851475143
a = 2
while True:
    if x % a == 0:
        x /= a
        if x == 1:
            print(a)
            break
        a = 1
    a += 1