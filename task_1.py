# Task 1
# add a comment describing the error and how to fix it.
# The following code is intended to calculate the sum of all even numbers between 1 and a given n. However, there is a bug in the code. Debug it using breakpoint() and print statements.
def calculate_sum(n):
    total = 0
    # breakpoint() # add breakpoint here
    for i in range(1, n+1):
        # print(f"i: {i}")  # Print i to see the bug
        if i % 2 != 0:   # if i % 2 == 0: -> Correct 
            # print(f"i: {i}")  # Print i to see the bug
            total += i
    return total

result = calculate_sum(10) 
print(result)

# 