i = 1
val = 0
n = 0
while n < 500:
    val += i
    n = 0
    a = int(val**0.5)
    for j in range(1, a + 1):
        if val % j == 0:
            b = val // j
            n += 1 + (j != b) * 1
    i += 1

print(f'{val}') 
 
