f = 1
for n in range(1, 101):
    f *= n

f_str = str(f)

s = 0
for h in f_str:
    s += int(h)

print(s)