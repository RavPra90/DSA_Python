# Delete an element at a specific position
def delete_element(arr, position):
    if position < len(arr):
        arr.pop(position)  # Using Python's built-in pop method
    else:
        print("Position out of range!")

# Example usage
array = [10, 20, 30, 40, 50]
delete_element(array, 2)
print("After Deletion:", array)


# we can also remove() method directly on array
array.remove(40) # remove take the value instead of index
print(array)

"""
Time complexity : O(N).
Space complexity for this method is constant because we don't need an extra location to perform this operation.
"""