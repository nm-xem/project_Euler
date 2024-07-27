dict_pal = []
for i in range(999, 999, -1):
    for j in range(999, i-1, -1):
        e = str(i*j)
        if e == e[::-1]:
            dict_pal.append(e)
m = int(dict_pal[0])
for p in dict_pal:
    if int(p) > m:
        m = int(p)
print(m)
# print(dict_pal)