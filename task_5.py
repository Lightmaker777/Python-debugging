# Task 5:
# The following code is an implementation of the bubble sort algorithm to sort a list. However, it's not sorting the list correctly. Use breakpoint() and print statements to debug the code and fix the sorting algorithm.

def bubble_sort(lst):
    n = len(lst)
    #breakpoint()  # Set a breakpoint
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]: # if lst[j] > lst[j + 1]: <- Correct the comparison condition
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(f"Iteration {i+1}: {lst}")  # Print the current state of the list
    return lst

result = bubble_sort([4, 2, 7, 1, 3])
print(result)
