#Traversal refers to accessing each element of the array sequentially.

# Traversing an array and printing each element
def traverse_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

# Example usage
array = [10, 20, 30, 40, 50]
print("Traversal:")
traverse_array(array)
#output :Traversal:
#10 20 30 40 50


"""
Time complexity : O(N).
Space complexity for this method is constant because we don't need an extra location to perform this operation.
"""