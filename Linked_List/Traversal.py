# Creating a Node class to represent each element (node) in the linked list

"""
Node Class:
Each node stores a value and a pointer to the next node.
When a node is created, its next pointer is initialized to None.
"""

class Node:
    def __init__(self, value):
        self.value = value  # Store the provided value in the node
        self.next = None  # Pointer to the next node; initially there is no next node

"""
Linked_List Class:
This class manages the linked list. It has three main attributes:

head: The first node in the list.
tail: The last node in the list.
length: The number of nodes in the list.
"""


# Creating a Linked List class to manage multiple nodes
class Linked_List:
    # Initializing the linked list constructor
    def __init__(self):
        self.head = None  # Points to the first node; None means the list is empty
        self.tail = None  # Points to the last node; None means the list is empty
        self.length = 0  # Keeps track of the number of nodes in the list

    """
    append Method:
    This method adds a new node with the given value at the end of the list.

    If the list is empty, the new node becomes both the head and tail.
    Otherwise, the new node is linked to the current tail, and then the tail is updated.
    """

    # Insert a node at the end of the list
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            self.tail = new_node  # Also set the new node as the tail since it's the only node
        else:
            self.tail.next = new_node  # Link the current tail's 'next' pointer to the new node
            self.tail = new_node  # Update the tail to be the new node
        self.length += 1  # Increase the count of nodes in the list

    """
    traverse Method:
    This method prints all the values in the linked list from the head to the tail.
    It starts at the head and moves through each node, printing its value followed by an arrow.
    At the end of the list, it prints "None" to indicate there are no more nodes.
    """

    def traverse(self):
        current = self.head  # Start with the head node
        while current:  # Continue until the end of the list is reached (current becomes None)
            print(current.value, end="->")  # Print the current node's value followed by an arrow
            current = current.next  # Move to the next node in the list
        print("None")  # Indicate the end of the list


# ----------------------- TEST CODE BELOW -----------------------
# The following code tests the append and traverse methods and prints the output for each scenario.

if __name__ == '__main__':
    # Create a new linked list instance
    ll = Linked_List()

    # Scenario 1: Append nodes to the list
    # Appending three nodes with values 10, 20, and 30.
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("After appending nodes with values 10, 20, 30:")

    # Scenario 2: Traverse the list to print its elements
    # This will print: 10->20->30->None
    ll.traverse()

    # Additional Scenario: Append more nodes to see the list grow
    ll.append(40)
    ll.append(50)
    print("After appending nodes with values 40, 50:")
    ll.traverse()
