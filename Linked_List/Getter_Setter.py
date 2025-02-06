# Creating a Node class to represent each element (node) in the linked list
class Node:
    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Parameters:
          value: The value to be stored in the node.
        """
        self.value = value  # Store the provided value in the node
        self.next = None  # Pointer to the next node; initially there is no next node


# Creating a Linked List class to manage multiple nodes
class Linked_List:
    def __init__(self):
        """
        Initializes an empty linked list.

        Attributes:
          head: Points to the first node in the list (None means the list is empty).
          tail: Points to the last node in the list (None means the list is empty).
          length: Tracks the number of nodes in the list.
        """
        self.head = None  # No head initially; list is empty
        self.tail = None  # No tail initially; list is empty
        self.length = 0  # Initially, there are zero nodes in the list

    """
     Returns a string representation of the linked list.

     The format will be: "value1 -> value2 -> value3"
     """

    def __str__(self):

        tempNode = self.head  # Start at the head of the list
        result = ''  # Initialize an empty string for the result
        while tempNode is not None:
            result += str(tempNode.value)  # Append the current node's value to the result
            if tempNode.next is not None:
                result += " -> "  # Add an arrow separator if there is another node
            tempNode = tempNode.next  # Move to the next node
        return result  # Return the complete string representation

        """
        Appends a new node with the specified value at the end of the linked list.

        Parameters:
          value: The value to be added to the list.

        Process:
          - If the list is empty, the new node becomes both the head and tail.
          - Otherwise, the new node is linked after the current tail, and the tail is updated.
        """
    def append(self, value):

        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set new node as the head
            self.tail = new_node  # Set new node as the tail
        else:
            self.tail.next = new_node  # Link the current tail's next pointer to the new node
            self.tail = new_node  # Update the tail to be the new node
        self.length += 1  # Increment the count of nodes in the list

        """
        Retrieves the node at the specified index.

        Parameters:
          index: The position of the node to retrieve. Use -1 to return the tail node.

        Returns:
          The node at the specified index if it exists, otherwise None.

        Process:
          - If index is -1, return the tail node.
          - If index is out of bounds, return None.
          - Otherwise, traverse the list from the head to the given index.
        """
    def get(self, index):

        if index == -1:
            return self.tail  # Special case: index -1 returns the tail node
        if index < -1 or index >= self.length:
            return None  # Return None if index is out of bounds
        current = self.head  # Start from the head of the list
        for _ in range(index):
            current = current.next  # Move through the list until reaching the specified index
        return current  # Return the node at the specified index


        """
        Updates the value of the node at the specified index.

        Parameters:
          index: The position of the node to update.
          value: The new value to be set in the node.

        Returns:
          True if the update was successful; False if no node was found at the given index.

        Process:
          - Retrieve the node using the get() method.
          - If the node exists, update its value.
        """
    def set(self, index, value):

        temp = self.get(index)  # Retrieve the node at the specified index
        if temp:  # Check if the node exists
            temp.value = value  # Update the node's value with the new value
            return True  # Indicate that the operation was successful
        return False  # Return False if no node was found at that index


# ----------------------- TEST CODE BELOW -----------------------
# The following code tests the functionality of the linked list methods.

if __name__ == '__main__':
    # Create a new linked list instance
    ll = Linked_List()
    print("Initial list (should be empty):", ll)  # Expected output: (empty string)

    # Scenario 1: Append nodes to the list
    ll.append(5)
    ll.append(10)
    ll.append(15)
    print("List after appending 5, 10, 15:", ll)
    # Expected output: "5 -> 10 -> 15"

    # Scenario 2: Get the node at index 0 (should return the node with value 5)
    node0 = ll.get(0)
    print("Node at index 0 (expected value 5):", node0.value if node0 else None)

    # Scenario 3: Get the node at index 1 (should return the node with value 10)
    node1 = ll.get(1)
    print("Node at index 1 (expected value 10):", node1.value if node1 else None)

    # Scenario 4: Get the node at index -1 (should return the tail node, with value 15)
    nodeTail = ll.get(-1)
    print("Node at index -1 (expected tail value 15):", nodeTail.value if nodeTail else None)

    # Scenario 5: Set the value at index 1 to 20
    success = ll.set(1, 20)
    print("Result of setting index 1 to 20 (should be True):", success)
    print("List after setting index 1 to 20:", ll)
    # Expected output: "5 -> 20 -> 15"

    # Scenario 6: Attempt to set the value at an out-of-range index (e.g., 3)
    success = ll.set(3, 25)
    print("Result of setting index 3 to 25 (should be False):", success)
    print("List after attempting to set index 3:", ll)
    # Expected output: "5 -> 20 -> 15" (unchanged)
