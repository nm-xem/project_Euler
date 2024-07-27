n = 600851475143
c = 2

while n > 1:
    if n % c != 0:
        if c > 2:
            c += 2
        else:
            c = 3
    else:
        n = n // c

print(c)