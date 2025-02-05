# Creating a Node class to represent each element (node) in the linked list
from numpy.f2py.crackfortran import traverse  # Imported but not used in this code


class Node:
    def __init__(self, value):
        self.value = value  # Store the given value in the node
        self.next = None  # Pointer to the next node; initially there is no next node


# Creating a Linked List class to manage multiple nodes
class Linked_List:
    # Initializing the linked list constructor
    def __init__(self):
        self.head = None  # Points to the first node (None means the list is empty)
        self.tail = None  # Points to the last node (None means the list is empty)
        self.length = 0  # Keeps track of the number of nodes in the list



    # This method returns a string representation of the list (e.g., "10 -> 20 -> 30")
    def __str__(self):
        tempNode = self.head  # Start from the head (first node)
        result = ''  # This string will accumulate the values of nodes
        while tempNode is not None:
            result += str(tempNode.value)  # Append the node's value to the string
            if tempNode.next is not None:
                result += " -> "  # If there's another node, add an arrow
            tempNode = tempNode.next  # Move to the next node in the list
        return result  # Return the complete string representation of the list



    # Insert a node at the end of the list
    def append(self, value):
        new_node = Node(value)  # Create a new node with the provided value
        if self.head is None:  # If the list is empty, set both head and tail to this node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the current tail node to the new node
            self.tail = new_node  # Update the tail to be the new node
        self.length += 1  # Increase the count of nodes in the list



    # Remove and return the first node's value
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



    # Remove and return the last node's value
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



    # Get the node at a specified index (use -1 to get the last node)
    def get(self, index):
        if index == -1:  # Special case: if index is -1, return the tail node
            return self.tail
        if index < -1 or index >= self.length:
            return None  # Return None if index is out of range
        current = self.head
        for _ in range(index):
            current = current.next  # Move to the next node until the index is reached
        return current  # Return the node at the specified index



    # Remove a node at a specific index and return its value
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
        prev_node.next = popped_node.next  # Link the previous node to the node after the one removed
        popped_node.next = None  # Disconnect the removed node
        self.length -= 1  # Decrease the node count



    # Delete all nodes in the list (reset the list to empty)
    def delete_all(self):
        self.head = None  # Remove reference to the first node
        self.tail = None  # Remove reference to the last node
        self.length = 0  # Reset the node count to zero


# ----------------------- TEST CODE BELOW -----------------------
# This part of the code demonstrates how each method works by printing outputs.

if __name__ == '__main__':
    # Create a new linked list instance
    ll = Linked_List()
    print("Initial list (should be empty):", ll)

    # Scenario 1: Append nodes to the list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    print("List after appending 10, 20, 30, 40:", ll)
    # Expected output: 10 -> 20 -> 30 -> 40

    # Scenario 2: Remove the first element
    popped_first = ll.pop_first()
    print("Popped first element (should be 10):", popped_first)
    print("List after popping first element:", ll)
    # Expected output: 20 -> 30 -> 40

    # Scenario 3: Remove the last element
    popped_last = ll.pop()
    print("Popped last element (should be 40):", popped_last)
    print("List after popping last element:", ll)
    # Expected output: 20 -> 30

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
    # Expected output: 30

    # Scenario 6: Append more values to test removal using index -1 (removes last element)
    ll.append(50)
    ll.append(60)
    print("List after appending 50 and 60:", ll)
    # Expected output: 30 -> 50 -> 60
    removed_last = ll.remove(-1)  # Remove the last element using -1 as index
    print("Removed element at index -1 (should be 60):", removed_last)
    print("List after removing element at index -1:", ll)
    # Expected output: 30 -> 50

    # Scenario 7: Delete all nodes from the list
    ll.delete_all()
    print("List after deleting all nodes (should be empty):", ll)
