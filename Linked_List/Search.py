# Creating a Node class to represent each element (node) in the linked list

"""
Node Class:
Each node stores a value and a pointer to the next node.
When a node is created, its next pointer is initialized to None.
"""
class Node:
    def __init__(self, value):
        self.value = value  # Store the provided value in the node
        self.next = None    # Pointer to the next node; initially there is no next node

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
        self.length = 0   # Keeps track of the number of nodes in the list

    """
    append Method:
    This method adds a new node with the given value at the end of the list.

    If the list is empty, the new node becomes both the head and tail.
    Otherwise, the new node is linked to the current tail, and then the tail is updated.
    """

    # Insert a node at the end of the list
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:   # If the list is empty
            self.head = new_node  # Set the new node as the head
            self.tail = new_node  # Also set the new node as the tail since it's the only node
        else:
            self.tail.next = new_node  # Link the current tail's 'next' pointer to the new node
            self.tail = new_node       # Update the tail to be the new node
        self.length += 1  # Increase the count of nodes in the list

    """
    search Method:
    This method checks whether a given target value exists in the list. It iterates through each node:

    If a node with the target value is found, it returns True.
    If the iteration completes without finding the value, it returns False.  
    """

    # Search for a target value in the list
    def search(self, target):
        current = self.head  # Start from the head node
        while current:  # Loop through the list until the end
            if current.value == target:  # Check if the current node's value matches the target
                return True  # If found, return True
            current = current.next  # Move to the next node
        return False  # If the target is not found in any node, return False




# ----------------------- TEST CODE BELOW -----------------------
# The following code tests the append and search methods and prints the output for each scenario.

if __name__ == '__main__':
    # Create a new linked list instance
    ll = Linked_List()

    # Scenario 1: Append nodes to the list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Nodes appended to the list: 10, 20, 30")

    # Scenario 2: Search for an existing value (20) in the list
    search_result = ll.search(20)
    print("Search for 20 (expected True):", search_result)

    # Scenario 3: Search for a non-existing value (40) in the list
    search_result = ll.search(40)
    print("Search for 40 (expected False):", search_result)

    # Scenario 4: Search for the first element (10) in the list
    search_result = ll.search(10)
    print("Search for 10 (expected True):", search_result)

    # Scenario 5: Search for the last element (30) in the list
    search_result = ll.search(30)
    print("Search for 30 (expected True):", search_result)
