import time

t1 = time.time()

flag = False
result = []
for a in range(1000):
    if flag:
        break
    for b in range(1000):
        if a + b > 1000 or flag:
            break
        if a == b:
            continue
        for c in range(1000):
            if a + b + c > 1000 or flag:
                break
            if b == c:
                continue
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    result = [a, b, c]
                    flag = True

t2 = time.time()

print(result)
print(f'{result[0]**2}, {result[1]**2}, {result[2]**2}')
print(f'{result[0]**2} + {result[1]**2}, {result[0]**2 + result[1]**2}')
print(t2-t1)

t3 = time.time()

flag = False
result = []
for a in range(1000):
    if flag:
        break
    for b in range(1000):
        if a == b:
            continue
        c = (a**2 + b**2)**0.5
        if b == c:
            continue
        if a + b + c > 1000 or flag:
            break
        if a + b + c == 1000:
            result = [a, b, c]
            flag = True

t4 = time.time()

print(result)
print(f'{result[0]**2}, {result[1]**2}, {result[2]**2}')
print(f'{result[0]**2} + {result[1]**2}, {result[0]**2 + result[1]**2}')
print(t4-t3)