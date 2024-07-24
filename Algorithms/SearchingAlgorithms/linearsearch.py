# my_list = [10,30,0,40,80]
# def linear_search(arr, target)
#     for i in range(len(arr))
#         if arr[1] == target:
#             return i
#         return -1

# for index, element in enumerate(my_list):

# def linear_search(my_list):
#     for index in range(len(my_list)):
#         element = my_list[index]
#         print(f"Index {index}: {element}")

# linear_search(my_list)

def linear_search(my_list, target):
    for index, element in enumerate(my_list):
        if element == target:
            return index, element
        else:
            # -1 means it is not found
            return -1


some_list = 10, 30, 0, 40, 80
answer = linear_search(some_list, 100)
print(f' Target found at index {answer}') if answer != -1 else print('Target not found')
