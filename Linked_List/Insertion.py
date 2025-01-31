# Creating a Node class to represent each element (node) in the linked list
class Node:
    def __init__(self, value):
        self.value = value  # Storing the value of the node
        self.next = None  # Pointer to the next node (initially None since there's no next node yet)

# Creating a Linked List class to manage multiple nodes
class Linked_List:
    # Initializing the linked list constructor
    def __init__(self):
        self.head = None  # Points to the first node (initially None, meaning the list is empty)
        self.tail = None  # Points to the last node (initially None, meaning the list is empty)
        self.length = 0   # Keeps track of the number of nodes in the list

    # Printing the complete linked list in a readable format
    def __str__(self):
        tempNode = self.head  # Start from the head node
        result = ''  # String to store the output representation of the linked list
        while tempNode is not None:
            result += str(tempNode.value)  # Add the node's value to the string
            if tempNode.next is not None:
                result += " -> "
            tempNode = tempNode.next  # Move to the next node
        return result  # Return the string representation of the list

    # Insert a node at the beginning of the list
    def prepend(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Point the new node to the current head
            self.head = new_node  # Update the head to the new node
        self.length += 1  # Increase the length of the list

    # Insert a node at a specific index in the list
    def insert(self, index, value):
        new_node = Node(value)  # Create a new node
        # Handling cases where the index is out of bounds
        if index < 0 or index > self.length:
            return False  # Return False to indicate invalid index
        # If the list is empty, set the new node as both head and tail
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # If inserting at the beginning, use the prepend logic
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head  # Start from the head
            for _ in range(index - 1):  # Traverse to the node just before the desired index
                temp_node = temp_node.next
            new_node.next = temp_node.next  # Link new node to the next node
            temp_node.next = new_node  # Link previous node to the new node
        self.length += 1  # Increase the length
        return True  # Return True to indicate successful insertion

    # Insert a node at the end of the list
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the last node to the new node
            self.tail = new_node  # Update the tail to the new node
        self.length += 1  # Increase the length

# Testing the Linked List functionality
ll = Linked_List()
print("Initial empty linked list:", ll)  # Should print an empty string

# Append values to the linked list
ll.append(10)
ll.append(20)
ll.append(30)
print("After appending 10, 20, 30:", ll)  # Expected: 10 -> 20 -> 30

# Prepend a value to the linked list
ll.prepend(5)
print("After prepending 5:", ll)  # Expected: 5 -> 10 -> 20 -> 30

# Insert at specific index
ll.insert(2, 15)
print("After inserting 15 at index 2:", ll)  # Expected: 5 -> 10 -> 15 -> 20 -> 30

# Insert at the beginning (index 0)
ll.insert(0, 1)
print("After inserting 1 at index 0:", ll)  # Expected: 1 -> 5 -> 10 -> 15 -> 20 -> 30

# Insert at the end (index = length)
ll.insert(ll.length, 40)
print("After inserting 40 at the last index:", ll)  # Expected: 1 -> 5 -> 10 -> 15 -> 20 -> 30 -> 40

# Try inserting at an invalid index
result = ll.insert(-1, 50)
print("Trying to insert at an invalid index (-1):", result)  # Expected: False
