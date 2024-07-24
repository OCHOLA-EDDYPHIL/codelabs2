def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if target is found
        elif arr[mid] < target:
            left = mid + 1  # Discard the left half
        else:
            right = mid - 1  # Discard the right half

    return -1  # Return -1 if target is not found


my_list = [1, 6, 5, 43, 8, 64, 88, 7, 45, 49, 92, 29]
my_list.sort()
answer = binary_search(my_list, 45)
print(f'Target was found at index {answer}')
print(f'Sorted list: {my_list}')
