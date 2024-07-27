import time

start = time.time()

sum_num = 0

for i in range(1000000000):
    if ((i % 3) == 0) or ((i % 5) == 0):
        sum_num += i

print(sum_num)
t = time.time() - start
print(t)
