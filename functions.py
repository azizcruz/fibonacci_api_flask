
# Use memoiazation for caching the repeated values.
fibonacci_cache = {}

def fibonacci(n):

    # if the value is cached then just return it.
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # handle if n is less than 3
    if 3 > n:
        value = 1
        if n == 0:
            value = 0
        
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # Cache the value then return it.
    fibonacci_cache[n] = value
    
    return value