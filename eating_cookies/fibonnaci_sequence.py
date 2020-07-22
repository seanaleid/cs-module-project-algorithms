from timeit import timeit

cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]

    if n <= 0:
        result = 0
    elif n <= 2 and n >= 0:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)

    cache[n] = result
    return result

print(fibonacci(104))
print(timeit('fibonacci(104)', globals=globals(), number=1))
print(fibonacci(35))
print(timeit('fibonacci(35)', globals=globals(), number=1))
print(fibonacci(4))
print(timeit('fibonacci(4)', globals=globals(), number=1))
print(fibonacci(83))
print(timeit('fibonacci(83)', globals=globals(), number=1))


# from timeit import timeit

# def memoize(func):
#     cache = dict()

#     def memoized_func(*args):
#         if args in cache:
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result
    
#     return memoized_func

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# WARNING! Can take between 5~10secs to complete.
# print(timeit('fibonacci(35)', globals=globals(), number=1))

# WARNING! Can take between 5~10secs to complete.
# memoized_fib = memoize(fibonacci)
# print(timeit('memoized_fib(5)', globals=globals(), number=1))
# print(timeit('memoized_fib(35)', globals=globals(), number=1))
# print(timeit('memoized_fib(35)', globals=globals(), number=1))
# print(memoized_fib.__closure__[0].cell_contents)
# print(memoized_fib(35))
# print(memoized_fib(1))
# print(memoized_fib(2))
# print(memoized_fib(3))
# print(memoized_fib(4))
# print(memoized_fib(5))
# print(memoized_fib.__closure__[0].cell_contents)
# print(timeit('memoized_fib(5)', globals=globals(), number=1))
# print(timeit('memoized_fib(35)', globals=globals(), number=1))