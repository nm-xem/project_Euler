import time

start = time.time()

def fib (a, b, sum_fib, list_fib):
    c = a
    a = b
    b = a + c
    if b < 4_000_000:
        list_fib.append(b)
        if b % 2 == 0:
            sum_fib += b
        req1, req2 = fib (a, b, sum_fib, list_fib)
    else:
        return list_fib, sum_fib
    return req1, req2
    

req1, req2 = fib (1, 2, 2, [1, 2])
print(f'{req1}\n{req2}')
t = time.time() - start
print(t)
