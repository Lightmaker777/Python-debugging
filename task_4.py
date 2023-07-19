# Task 4:
# The code snippet below is meant to check if a number is prime or not. However, it returns incorrect results for some inputs. Use breakpoint() and print statements to debug the code and make it work correctly.

def is_prime(number):
    if number < 2:
        return False
    #breakpoint()  # Set a breakpoint
    for i in range(2, number):
        print(f"number: {number}, i: {i}") # for i in range(2, number//2 + 1): -> Correct the range
        if number % i == 0:
            return False
    return True

result = is_prime(10)
print(result)
