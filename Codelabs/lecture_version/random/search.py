import math

# search if 36 exist
# def search_array(x, y):
#     for item in x:
#         if item == y:
#             return True
#     return False


#     if query in array:
#         return True
#     return False
array = [10, 9, 4, 36, 48, 71, 81]


# query = 5
# print(search_array(array, query))

#seach and return perfect square

def perfect_square(x):
    for item in x:
        root = math.sqrt(item)
        if root.is_integer():
            print(item)


perfect_square(array)
