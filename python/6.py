import time

dict_nums = {val: val**2 for val in range(1,100000001)}

sum_sq = 0
summ = 0

t1 = time.time()
for i, i2 in dict_nums.items():
    sum_sq += i2
    summ += i
sq_sum = summ**2

t2 = time.time()

print(sq_sum-sum_sq, t2-t1)

list_1 = [val for val in range(1,100000001)]
list_2 = [val**2 for val in range(1,100000001)]

t3 = time.time()

sum_sq = sum(list_2)
sq_sum = sum(list_1)**2

t4 = time.time()

print(sq_sum-sum_sq, t4-t3)