"""
The following function is supposed to find two numbers in an array that when summed up form the target
"""

def summation(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]+array[j] == target:
                return array[i], array[j]
    return None        

myarr = [10, 9,7, 2,1]
target = 10
print(f"the numbers are{summation(myarr, target)}")    