def max_min_divide_conquer(arr, low, high):
    # Define a Pair class to hold the maximum and minimum values found
    class Pair:
        def __init__(self):
            self.max = float('-inf')  # Initialize max to negative infinity
            self.min = float('inf')  # Initialize min to positive infinity

    result = Pair()  # Create an instance of Pair to store the result

    # If there is only one element, it is both the max and min
    if low == high:
        result.max = arr[low]
        result.min = arr[low]
        return result

    # If there are two elements, compare them to find the max and min
    if high == low + 1:
        if arr[low] < arr[high]:
            result.min = arr[low]
            result.max = arr[high]
        else:
            result.min = arr[high]
            result.max = arr[low]
        return result

    # If there are more than two elements, divide the array into halves
    mid = (low + high) // 2
    left_result = max_min_divide_conquer(arr, low, mid)  # Recurse on the left half
    right_result = max_min_divide_conquer(arr, mid + 1, high)  # Recurse on the right half

    # Compare the results from the two halves to find the overall max and min
    result.max = max(left_result.max, right_result.max)
    result.min = min(left_result.min, right_result.min)

    return result  # Return the final result containing the max and min


# Example usage
arr = [6, 4, 26, 14, 33, 64, 46]  # Sample array
result = max_min_divide_conquer(arr, 0, len(arr) - 1)  # Find max and min
print("Maximum element is:", result.max)  # Print the maximum element
print("Minimum element is:", result.min)  # Print the minimum element
