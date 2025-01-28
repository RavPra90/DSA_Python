import array

def accessElement(array, index):
    if index >=len(array):
        print ("Index element is greater than size of Array!")
    else:
        print(array[index])

my_array= [1,2,3,4,5]
accessElement(my_array,3)   #Output: 4
accessElement(my_array,8)  #Output : Index element is greater than size of Array!

"""
Time complexity :O(1) 
Space complexity : O(1) as  we don't need extra space here to to perform this operation.

"""