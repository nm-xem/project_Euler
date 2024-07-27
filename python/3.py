import time

start = time.time()

n = 60085147514309
c = 2
list_simple = []

while n > 1:
    if n % c != 0:
        if c > 2:
            c += 2
        else:
            c = 3
    else:
        n = n / c
        if c not in list_simple:
            list_simple.append (c)

print(list_simple)
t = time.time() - start
print(t)