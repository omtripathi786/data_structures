def get_fib(n):
    if n <= 1:
        return n
    else:
        return get_fib(n - 1) + get_fib(n - 2)


    return -1

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)