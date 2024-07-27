def fib (a, b, sum_fib):
    c = a + b
    if c <= 4_000_000:
        if c % 2 == 0:
            sum_fib += c
        sum_fib = fib (b, c, sum_fib)
    else:
        return sum_fib
    return sum_fib
    
sum_fib = fib (1, 2, 2)
print(f'{sum_fib}')