def arr_sum(arr, num):
    global full
    arr1 = [num]
    full = arr1 + arr
    return full

nums = [10, 20, 34, 42, 33]
print(arr_sum(nums, 2))
print(arr_sum(nums, 2))
print(arr_sum(nums, 2))