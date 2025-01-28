 #Python Array Methods
from array import *


#  1. `append(element)`
# Adds an element to the end of the array.
arr = [1, 2, 3]
arr.append(4)
print(arr)  # Output: [1, 2, 3, 4]

# - Use Case: Adding single elements dynamically.
# - Time Complexity: \( O(1) \) (on average).



#  2. `extend(iterable)`
# Adds all the elements of an iterable (like another list) to the array.
arr = [1, 2, 3]
arr.extend([4, 5, 6])
print(arr)  # Output: [1, 2, 3, 4, 5, 6]

# - Use Case: Concatenating multiple lists.
# - Time Complexity: \( O(k) \) (k = number of elements in the iterable).



#  3. `insert(index, element)`
# Inserts an element at a specified index.
arr = [1, 2, 4]
arr.insert(2, 3)  # Insert 3 at index 2
print(arr)  # Output: [1, 2, 3, 4]

# - Use Case: Adding elements at specific positions.
# - Time Complexity: \( O(n) \) (elements after the index must be shifted).



#  4. `remove(element)`
# Removes the first occurrence of a specified element.
arr = [1, 2, 3, 2]
arr.remove(2)  # Removes the first occurrence of 2
print(arr)  # Output: [1, 3, 2]

# - Use Case: Removing specific elements.
# - Time Complexity: \( O(n) \) (searching for the element).



#  5. `pop([index])`
# Removes and returns an element at the given index (default: last element).
arr = [1, 2, 3, 4]
removed = arr.pop(2)  # Removes the element at index 2
print(arr)     # Output: [1, 2, 4]
print(removed) # Output: 3

# - Use Case: Dynamically removing elements.
# - Time Complexity: \( O(1) \) (if the last element is removed); \( O(n) \) for other indices.



#  6. `index(element, start, end)`
# Returns the index of the first occurrence of the element.
arr = [1, 2, 3, 2]
index = arr.index(2)  # Finds the first occurrence of 2
print(index)  # Output: 1

# - Use Case: Locating an element.
# - Time Complexity: \( O(n) \).



#  7. `count(element)`
# Returns the count of occurrences of the specified element.
arr = [1, 2, 2, 3, 2]
count = arr.count(2)  # Counts the occurrences of 2
print(count)  # Output: 3

# - Use Case: Counting duplicates.
# - Time Complexity: \( O(n) \).



#  8. `reverse()`
# Reverses the order of the elements in the array.
arr = [1, 2, 3, 4]
arr.reverse()
print(arr)  # Output: [4, 3, 2, 1]

# - Use Case: Reversing arrays in place.
# - Time Complexity: \( O(n) \).



#  9. `sort(key=None, reverse=False)`
# Sorts the array in ascending order (default).
arr = [4, 2, 3, 1]
arr.sort()
print(arr)  # Output: [1, 2, 3, 4]

# Sort in descending order
arr.sort(reverse=True)
print(arr)  # Output: [4, 3, 2, 1]

# - Use Case: Sorting data.
# - Time Complexity: \( O(n \log n) \).



#  10. `copy()`
# Returns a shallow copy of the array.
arr = [1, 2, 3]
copy_arr = arr.copy()
copy_arr.append(4)

print(arr)      # Output: [1, 2, 3]
print(copy_arr) # Output: [1, 2, 3, 4]

# - Use Case: Duplicating arrays without modifying the original.
# - Time Complexity: \( O(n) \).



#  11. `clear()`
# Removes all elements from the array.
arr = [1, 2, 3]
arr.clear()
print(arr)  # Output: []

# - Use Case: Resetting arrays.
# - Time Complexity: \( O(1) \).

#12. tobytes()
# Converts teh array to string
array = array("i", [1,2,3,4])
print(array.tobytes())
