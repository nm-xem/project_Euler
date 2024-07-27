max_num = 0
for i in range(999, 99, -1):
    for j in range(999, i-1, -1):
        num = i*j
        if num < max_num:
            break
        num_str = str(num)
        if num_str == num_str[::-1]:
            max_num = num

print(max_num)