#Task 3:
#The following code is supposed to find the maximum value in a list, but it's not returning the correct result. Debug the code using breakpoint() and print statements to fix the issue.

def find_max(numbers):
    max_value = numbers[0] #max_value = float('-inf') -> Correct the initialization
    for number in numbers:
        if number > max_value:
            max_value = number
        print(f"number: {number}, max_value: {max_value}")  # Print number and max_value    
    #breakpoint()  # Set a breakpoint       
    return max_value

result = find_max([3, 8, 2, 5, 10])
print(result)  