"""
We can insert the element
    at the beginning of the array.
    in the middle of the array,
    at the end of the array.
"""
# Insert an element at a specific position
def insert_element(arr, element, position):
    arr.insert(position, element)  # Using Python's built-in insert method

# Example usage
array = [10, 20, 30, 40, 50]
insert_element(array, 25, 2)
print("\nAfter Insertion:", array)  #After Insertion: [10, 20, 25, 30, 40, 50]

"""
Worst Case: When we are inserting an element at the beginning of the array, the time complexity will be O(N)

space complexity of inserting an element into an array using array model is going to be O(1)
Because here when we are inserting the element, we need only one place for that element.
"""