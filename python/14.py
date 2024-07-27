import time

t1 = time.time()

max_i = 0
max_val = 0
for n in range(10, 1000000, 1):
    x = n
    i = 0
    while n > 1:
        i += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    if i > max_i:
        max_i = i
        max_val = x

t2 = time.time()

print(max_i, max_val, t2-t1)

t3 = time.time()

max_i = 0
max_val = 0
dict_r = {}
for n in range(2, 1000000, 1):
    x = n
    i = 0
    while n > 1:
        i += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n in dict_r:
            i += dict_r[n]
            n = 1
    dict_r[x] = i
    if i > max_i:
        max_i = i
        max_val = x

t4 = time.time()

print(max_i, max_val, t4-t3)
    
t5 = time.time()

max_i = 0
max_val = 0
dict_r = {}
for n in range(2, 1000000, 1):
    x = n
    i = 0
    while n > 1:
        i += 1
        if n & 1 == 0:
            n = n >> 2
        else:
            n = 3 * n + 1
        if n in dict_r:
            i += dict_r[n]
            n = 1
    dict_r[x] = i
    if i > max_i:
        max_i = i
        max_val = x

t6 = time.time()

print(max_i, max_val, t6-t5)