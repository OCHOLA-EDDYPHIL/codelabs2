def find_two_smallest(numbers):
    # Pre-condition: Ensure the input list contains at least two integers
    assert len(numbers) >= 2, "Input list must contain at least two integers."

    # Pre-condition: Ensure the input list only contains integers
    assert all(isinstance(x, int) for x in numbers), "Input list must only contain integers."

    # Initialize variables to store the smallest and second-smallest numbers
    smallest = second_smallest = float('inf')  # Initialize to infinity

    # Iterate through the list to find the two smallest numbers
    for num in numbers:

        # Check if the current number is smaller than the smallest number found so far
        if num < smallest:
            second_smallest = smallest  # Update the second smallest to the previous smallest
            smallest = num  # Update the smallest number

        # Check if the current number is smaller than the second-smallest number found so far
        elif num < second_smallest:
            second_smallest = num  # Update the second-smallest number

    # Return the two smallest numbers
    return smallest, second_smallest


# Test the function
numbers = [5, 3, 9, 1, 7]
result = find_two_smallest(numbers)
print("The two smallest numbers are:", result)
