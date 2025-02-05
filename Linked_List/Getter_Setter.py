# Creating a Node class to represent each element (node) in the linked list
class Node:
    def __init__(self, value):
        self.value = value  # Store the provided value in the node
        self.next = None    # Pointer to the next node; initially there is no next node

# Creating a Linked List class to manage multiple nodes
class Linked_List:
    # Initializing the linked list constructor
    def __init__(self):
        self.head = None   # Points to the first node in the list (None means the list is empty)
        self.tail = None   # Points to the last node in the list (None means the list is empty)
        self.length = 0    # Tracks the number of nodes in the list



    # This method returns a string representation of the list (e.g., "5 -> 10 -> 15")
    def __str__(self):
        tempNode = self.head  # Start from the head (first node)
        result = ''           # This string will hold the list representation
        while tempNode is not None:
            result += str(tempNode.value)  # Add the node's value to the string
            if tempNode.next is not None:
                 result += " -> "         # If there is another node, add an arrow separator
            tempNode = tempNode.next        # Move to the next node
        return result  # Return the complete string representation of the list



    # Append a node at the end of the list
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:   # If the list is empty, make the new node both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the current tail node to the new node
            self.tail = new_node       # Update the tail to be the new node
        self.length += 1  # Increase the count of nodes in the list



    # Get the node at a specific index (using -1 returns the tail node)
    def get(self, index):
        if index == -1:
            return self.tail  # Special case: -1 returns the last node in the list
        if index < -1 or index >= self.length:
            return None      # If index is out of valid range, return None
        current = self.head
        for _ in range(index):
            current = current.next  # Move through the list until reaching the desired index
        return current  # Return the node at the specified index



    #set the value of a node at the specified index
    def set(self, index, value):
        temp = self.get(index)  # Get the node at the specified index
        if temp:                # If the node exists,
            temp.value = value  # update its value
            return True         # Indicate that the operation was successful
        return False            # Return False if no node was found at that index



# ----------------------- TEST CODE BELOW -----------------------
# The following code tests the improved set method along with other methods.

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

    # Scenario 3: Attempt to set the value at an out-of-range index (e.g., 3)
    success = ll.set(3, 25)
    print("Result of setting index 3 to 25 (should be False):", success)
    print("List after attempting to set index 3:", ll)
    # Expected output: "5 -> 20 -> 15" (unchanged)