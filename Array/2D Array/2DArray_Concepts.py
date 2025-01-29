import numpy as np

#CREATION
"""
Time Complexity : O(mn)
Space Complexity : O(mn)
"""

twoDArray = np.array([ [11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

#INSERTION
"""
There are two different ways of adding elements in two dimensional array.
The first one is addition of columns and the second one is addition of rows.
Axis = 0 (new row will be added )
Axis = 1 (new colm will be added)

Time Complexity : O(mn)
Space Complexity : O(mn)
"""
#using Insert
newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)

print(len(twoDArray))

#using append
#append function, we can add row or column at the end of two dimensional array.
newTwoDArray = np.append(twoDArray, [[5,6,7,8]], axis=0)
print(newTwoDArray)
print(len(newTwoDArray))    #Output:5
print(len(newTwoDArray[0]))   #Output:4


#Access
"""
Time Complexity : O(1)
Space Complexity : O(1)
"""
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]): #  len(array) denotes row and len(array[0]) denotes colm
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

accessElements(newTwoDArray, 1, 2)     #Output:11


#Traverse
"""
Time Complexity O(mn) m= row n= colm
Space complexit = O(1)
"""
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end= " ")
        print()

traverseTDArray(twoDArray)


#SEARCH
"""
Time Complexity O(mn) m= row n= colm
Space complexit = O(1)
"""

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element no found'


print(searchTDArray(twoDArray, 12))  #Output: The value is located index 2 0

#DELETION
newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)