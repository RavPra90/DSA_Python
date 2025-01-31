
#creating a Node class
class Node:
    def __init__(self, value):
        self.value= value
        self.next= None

#Creating a Empty Linked list
class EmptyLL:
    def __init__(self):
        self.head= None
        self.tail= None
        self.length =0

#creating a Linked List class with 1 node where head and tail points to same node.
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head= new_node
        self.tail = new_node
        self.length = 1

new_ll= LinkedList(10)
print(new_ll.head.value)  #Output :10
print(new_ll.tail.value)  #Output :10

"""
Time Complexity :O(1)
Space Complexity :O(1)
"""