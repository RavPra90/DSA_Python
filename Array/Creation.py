import array
my_array = array.array("i") # i denotes storing integers only  Time Complexity = Space Complexity =  O(1)
print(my_array)  #Output: array('i')

my_array1= array.array("i", [1,2,3,4,5])   #Time Complexity = Space Complexity =   O(N)
print(my_array1)  # array('i', [1, 2, 3, 4, 5])


"""
Now, the next model that we can use for creating the array is going to be numpy model.
The advantage of numpy module is that it provides a feature rich and high performance array object,
and it is supporting the wide range of numerical operations and functions.
The disadvantage is that it is not part of the Python standard library, so you have to install additional

"""
import numpy as np
np_array = np.array([],dtype= int )  #Time Complexity = Space Complexity =   O(1)
print(np_array)  # Output: []

np_array1 = np.array([1,2,3,4,5])   # Time Complexity = Space Complexity =  O(N)
print(np_array1)  # Output : [1 2 3 4 5]

"""
The time and space complexity for creating the arrays with elements is O(N),
because both the time taken to copy the elements and the memory allocation for the elements depend
on the number of the elements 
For empty arrays, both time and space complexity are constant, since
there are no elements to copy or allocate memory for.
    
"""