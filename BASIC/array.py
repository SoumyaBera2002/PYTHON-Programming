import numpy as np

''' myarr = np.array([1,2,3,4,5,6])
print(myarr) '''

length = int(input("Enter the length of the array: "))
user_arr = []

for i in range(length):
    num = int(input("Enter the element for position " + str(i) + ": "))
    user_arr.append(num)

print("User-defined array:", user_arr)
