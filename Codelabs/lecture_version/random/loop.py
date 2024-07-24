# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

list_of_numbers = [10,30,0,2,43,1,-68,100]
target = 110
for num in list_of_numbers:
    if list_of_numbers[num]==target:
        # return True
        print(f'Number found at index {num}')
    # return False
    print(f'Not found')