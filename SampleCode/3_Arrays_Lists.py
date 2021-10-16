import array
import numpy as np
from sys import getsizeof


# array sample (slide 17)
import array
x = array.array('i')  # creates empty array of integers
x.append(10)
x.append(9)
x.append(8)
x.append(7)
x.append(5)

print(x[0])
x[0] = 100
print(x[0])

y = array.array('i', [10, 9, 8, 7, 5]) # creates an initialized array

print(y)


ARRAY_SIZE = 1000
array_data = np.linspace(1, ARRAY_SIZE, ARRAY_SIZE, dtype=int)

# CREATE A NEW ARRAY OF INTEGERS
x = array.array('i', array_data)

# VERY BASIC INTRO TO NUMPY ARRAYS
my_array = np.array([1, 2, 3, 4, 5])

for i in range(0,my_array.size):
    print(f"my_array[{i}] = {my_array[i]}")

my_big_array = np.array(array_data)

my_big_list = my_big_array.tolist()

#2d array
r1 = np.array([0, 1, 2, 3, 4])
r2 = np.array([0, 1, 2, 3])
two_d_array = np.array([r1, r2], dtype="object") # np doesn't like jagged arrays so you have to set dtype

print(two_d_array)

my_big_array = np.array(array_data)
print(my_big_array[0:5])    # Subselects first 5 elements

my_by_array_x_10 = my_big_array * 10

print(my_by_array_x_10)

print("Original 2-D Array")
print(two_d_array)
print("2-D Array x 2")
print(two_d_array * 2)

# COMPARE THE SIZES OF THE ARRAYS
print(f" Array Size: {getsizeof(x)} bytes for {len(x)} elements.")
print(f" Numpy Array Size: {getsizeof(my_big_array)} bytes bytes for {len(my_big_array)} elements..")
print(f" List Size: {getsizeof(my_big_list)} bytes bytes for {len(my_big_list)} elements.")

