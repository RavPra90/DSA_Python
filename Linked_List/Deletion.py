# Creating a Node class to represent each element (node) in the linked list
class Node:
    """
    __init__:
    Initializes a new node with the provided value.

    Parameters:
      value: The value to be stored in the node.

    Attributes:
      value: Stores the given value.
      next: Pointer to the next node (initially None).
    """

    def __init__(self, value):
        self.value = value  # Store the given value in the node
        self.next = None  # Pointer to the next node; initially there is no next node


# Creating a Linked List class to manage multiple nodes
class Linked_List:
    """
    __init__:
    Initializes an empty linked list.

    Attributes:
      head: Points to the first node (None means the list is empty).
      tail: Points to the last node (None means the list is empty).
      length: Tracks the number of nodes in the list.
    """

    def __init__(self):
        self.head = None  # Points to the first node in the list (empty initially)
        self.tail = None  # Points to the last node in the list (empty initially)
        self.length = 0  # Initially, there are zero nodes in the list

    """
    __str__:
    Returns a string representation of the linked list.

    Format Example: "10 -> 20 -> 30"
    """

    def __str__(self):
        tempNode = self.head  # Start from the head (first node)
        result = ''  # This string will accumulate the values of nodes
        while tempNode is not None:
            result += str(tempNode.value)  # Append the node's value to the string
            if tempNode.next is not None:
                result += " -> "  # If there's another node, add an arrow
            tempNode = tempNode.next  # Move to the next node in the list
        return result  # Return the complete string representation of the list

    """
    append:
    Inserts a new node with the provided value at the end of the linked list.

    Process:
      - If the list is empty, the new node becomes both the head and tail.
      - Otherwise, the new node is linked after the current tail, and the tail is updated.

    Parameters:
      value: The value to be added.
    """

    def append(self, value):
        new_node = Node(value)  # Create a new node with the provided value
        if self.head is None:  # If the list is empty, make the new node both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the current tail node to the new node
            self.tail = new_node  # Update the tail to be the new node
        self.length += 1  # Increase the count of nodes in the list

    """
    pop_first:
    Removes and returns the first node's value from the linked list.

    Process:
      - If the list is empty, returns None.
      - If there's only one node, empties the list.
      - Otherwise, updates the head to the next node and disconnects the removed node.

    Returns:
      The value of the removed node.
    """

    def pop_first(self):
        if self.length == 0:  # If the list is empty, there's nothing to remove
            return None
        popped_node = self.head  # Store the current head node as it will be removed
        if self.length == 1:
            # If there is only one node, removing it empties the list
            self.head = None
            self.tail = None
        else:
            # Move the head pointer to the next node
            self.head = self.head.next
            popped_node.next = None  # Disconnect the removed node from the list
        self.length -= 1  # Decrease the count of nodes
        return popped_node.value  # Return the value of the removed node

    """
    pop:
    Removes and returns the last node's value from the linked list.

    Process:
      - If the list is empty, returns None.
      - If there's only one node, empties the list.
      - Otherwise, traverses the list to find the node just before the tail, updates the tail,
        and disconnects the removed node.

    Returns:
      The value of the removed node.
    """

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail  # Store the current tail node to remove it later
        if self.length == 1:
            # If there's only one node, removing it empties the list
            self.head = self.tail = None
        else:
            # Traverse the list to find the node just before the tail
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None  # Disconnect the last node
            self.tail = temp  # Update the tail to be the previous node
        self.length -= 1  # Decrease the count of nodes
        return popped_node.value  # Return the value of the removed node

    """
    get:
    Retrieves the node at a specified index in the linked list.

    Parameters:
      index: The position of the node to retrieve. Use -1 to get the last node.

    Returns:
      The node at the specified index if it exists, otherwise None.

    Process:
      - If index is -1, returns the tail node.
      - If index is out of range, returns None.
      - Otherwise, traverses from the head to the specified index.
    """

    def get(self, index):
        if index == -1:  # Special case: if index is -1, return the tail node
            return self.tail
        if index < -1 or index >= self.length:
            return None  # Return None if index is out of valid range
        current = self.head
        for _ in range(index):
            current = current.next  # Move through the list until reaching the desired index
        return current  # Return the node at the specified index

    """
    remove:
    Removes a node at a specific index from the linked list.

    Parameters:
      index: The position of the node to remove. Use -1 to remove the last node.

    Process:
      - If the index is out of range, returns None.
      - If the index is 0, removes the first node.
      - If the index is the last element (or -1), removes the last node.
      - Otherwise, removes the node in the middle and adjusts pointers accordingly.

    Returns:
      The value of the removed node, if removal is successful.
    """

    def remove(self, index):
        # Check if the index is out of range (-1 represents the last element)
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()  # Remove the first element
        if index == self.length - 1 or index == -1:
            return self.pop()  # Remove the last element
        # For removal in the middle:
        prev_node = self.get(index - 1)  # Get the node just before the one to remove
        popped_node = prev_node.next  # The node to be removed
        prev_node.next = popped_node.next  # Link the previous node to the node after the removed node
        popped_node.next = None  # Disconnect the removed node
        self.length -= 1  # Decrease the node count
        return popped_node.value  # Return the value of the removed node

    """
    delete_all:
    Deletes all nodes in the linked list, effectively resetting it to empty.

    Process:
      - Removes references to the head and tail.
      - Resets the node count to zero.
    """

    def delete_all(self):
        self.head = None  # Remove reference to the first node
        self.tail = None  # Remove reference to the last node
        self.length = 0  # Reset the node count to zero


# ----------------------- TEST CODE BELOW -----------------------
# This part of the code demonstrates how each method works by printing outputs.

if __name__ == '__main__':
    # Create a new linked list instance
    ll = Linked_List()
    print("Initial list (should be empty):", ll)  # Expected output: (empty string)

    # Scenario 1: Append nodes to the list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    print("List after appending 10, 20, 30, 40:", ll)
    # Expected output: "10 -> 20 -> 30 -> 40"

    # Scenario 2: Remove the first element
    popped_first = ll.pop_first()
    print("Popped first element (should be 10):", popped_first)
    print("List after popping first element:", ll)
    # Expected output: "20 -> 30 -> 40"

    # Scenario 3: Remove the last element
    popped_last = ll.pop()
    print("Popped last element (should be 40):", popped_last)
    print("List after popping last element:", ll)
    # Expected output: "20 -> 30"

    # Scenario 4: Get the node at index 1 (should be the node with value 30)
    node_at_index = ll.get(1)
    if node_at_index:
        print("Element at index 1 (should be 30):", node_at_index.value)
    else:
        print("No element found at index 1")

    # Scenario 5: Remove the element at index 0 (this will remove the first element, 20)
    removed_value = ll.remove(0)
    print("Removed element at index 0 (should be 20):", removed_value)
    print("List after removing element at index 0:", ll)
    # Expected output: "30"

    # Scenario 6: Append more values to test removal using index -1 (removes last element)
    ll.append(50)
    ll.append(60)
    print("List after appending 50 and 60:", ll)
    # Expected output: "30 -> 50 -> 60"
    removed_last = ll.remove(-1)  # Remove the last element using -1 as index
    print("Removed element at index -1 (should be 60):", removed_last)
    print("List after removing element at index -1:", ll)
    # Expected output: "30 -> 50"

    # Scenario 7: Delete all nodes from the list
    ll.delete_all()
    print("List after deleting all nodes (should be empty):", ll)
