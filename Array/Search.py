#Searching for an element in the array involves checking each element until the desired value is found.
#Search Operation in Array is Linear.


# Linear search to find the index of an element
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
array = [10, 20, 30, 40, 50]
index = linear_search(array, 30)
print("Search Result:", index)

"""
Time complexity :O(1) 
Space complexity : O(1) as  we don't need extra space here to to perform this operation.

"""