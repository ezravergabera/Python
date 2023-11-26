## icecream

from icecream import ic

# def add(x, y):
#     return x + y

# # ic(add(10, 20))
# # ic(add(40, 20))
# # ic(add(10, 60))

# # result = ic(add(27,19))
# # print(result)

# def output_to_file(text):
#     with open("debug_log.txt", "a") as f:
#         f.write(text + '\n')


# ic.configureOutput(prefix="Debug| ", outputFunction=output_to_file, includeContext=True)

# ic(add(10, 20))

## Recursion

## Testing
# def getFactorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * getFactorial(n-1)

# ic(getFactorial(100))


import time as t

# Solution
def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_recursive_factorial(n-1)
    
def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        factorial = 1
        for x in range (1, n+1):
            factorial = factorial * x
        return factorial

start = ic(t.perf_counter())

ic(get_recursive_factorial(99))

ic(t.perf_counter() - start)

start = ic(t.perf_counter())

ic(get_iterative_factorial(99))

ic(t.perf_counter() - start)