# Task 2:
# The code below is an implementation of the factorial function. However, it contains a bug that causes an infinite loop. Use breakpoint() and print statements to identify and fix the bug.

def factorial(n):
    result = 1
    #breakpoint() # set a breakpoint here
    for i in range(n, 2, -1): # for i in range(n, 1, -1): -> Correct the range
        print(f"i: {i}, result: {result}")
        result *= i
        
    return result

result = factorial(5)
print(result)