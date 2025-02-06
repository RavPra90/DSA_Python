# Creating a Node class to represent each element (node) in the linked list
class Node:
    def __init__(self, value):
        self.value = value  # Storing the value of the node
        self.next = None    # Pointer to the next node (initially None since there's no next node yet)

"""
Linked_List Class:
This class manages the linked list. It has three main attributes:
  - head: The first node in the list.
  - tail: The last node in the list.
  - length: The number of nodes in the list.
"""
class Linked_List:
    # Description: Initializes a new empty linked list.
    def __init__(self):
        self.head = None  # Points to the first node (None means the list is empty)
        self.tail = None  # Points to the last node (None means the list is empty)
        self.length = 0   # Keeps track of the number of nodes in the list

    """
        __str__:
        Returns a string representation of the list.
        It traverses the list from head to tail and joins the node values with " <-> ".
        """
    def __str__(self):
        tempNode = self.head  # Start from the head node
        result = ''  # String to store the output representation of the linked list
        while tempNode is not None:
            result += str(tempNode.value)  # Add the node's value to the string
            if tempNode.next is not None:
                result += " -> "  # Add an arrow if there's another node
            tempNode = tempNode.next  # Move to the next node
        return result  # Return the complete string representation of the list

    """
     Description: Inserts a node at the beginning of the list.
     If the list is empty, the new node becomes both the head and tail.
     Otherwise, the new node is set to point to the current head and then becomes the new head.
    """
    def prepend(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set new node as head
            self.tail = new_node  # Set new node as tail also
        else:
            new_node.next = self.head  # Link new node to the current head
            self.head = new_node  # Update the head to the new node
        self.length += 1  # Increase the length of the list

    """
     Description: Inserts a node at a specific index in the list.
     If the index is invalid (less than 0 or greater than the list length), it returns False.
     For index 0, the method behaves like prepend.
     For any other valid index, it traverses to the appropriate position and inserts the new node.
    """

    def insert(self, index, value):
        new_node = Node(value)  # Create a new node with the given value
        # Handling cases where the index is out of bounds.
        if index < 0 or index > self.length:
            return False  # Return False to indicate invalid index

        # If the list is empty, set the new node as both head and tail.
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # If inserting at the beginning, use the prepend logic.
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head  # Start from the head
            # Traverse to the node just before the desired index.
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next  # Link new node to the next node
            temp_node.next = new_node  # Link previous node to the new node
            # If inserting at the end, update the tail pointer.
            if index == self.length:
                self.tail = new_node
        self.length += 1  # Increase the length of the list
        return True  # Return True to indicate successful insertion


    """
     Description: Appends a node at the end of the list.
     If the list is empty, the new node becomes both the head and tail.
     Otherwise, the new node is linked to the current tail, and then the tail is updated.
    """
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            self.tail = new_node  # Also set the new node as the tail
        else:
            self.tail.next = new_node  # Link the current tail's next pointer to the new node
            self.tail = new_node  # Update the tail to the new node
        self.length += 1  # Increase the length of the list



# ----------------------- TEST SCENARIOS BELOW -----------------------
# The following test scenarios demonstrate the functionality of the linked list with different cases.

if __name__ == '__main__':
    # Scenario 1: Creating an empty linked list and printing it.
    ll1 = Linked_List()
    print("Scenario 1: Initial empty linked list:")
    print(ll1)  # Expected output: "" (an empty string)

    # Scenario 2: Appending nodes to the list.
    ll2 = Linked_List()
    ll2.append(100)
    ll2.append(200)
    ll2.append(300)
    print("\nScenario 2: After appending 100, 200, 300:")
    print(ll2)  # Expected output: "100 -> 200 -> 300"

    # Scenario 3: Prepending a node to the list.
    ll3 = Linked_List()
    ll3.append(100)
    ll3.append(200)
    print("\nScenario 3: Before prepending, list is:")
    print(ll3)  # Expected: "100 -> 200"
    ll3.prepend(50)
    print("After prepending 50:")
    print(ll3)  # Expected: "50 -> 100 -> 200"

    # Scenario 4: Inserting a node in the middle of the list.
    ll4 = Linked_List()
    ll4.append(10)
    ll4.append(30)
    print("\nScenario 4: Before inserting, list is:")
    print(ll4)  # Expected: "10 -> 30"
    ll4.insert(1, 20)  # Insert 20 at index 1.
    print("After inserting 20 at index 1:")
    print(ll4)  # Expected: "10 -> 20 -> 30"

    # Scenario 5: Inserting at the beginning (index 0) using the insert method.
    ll5 = Linked_List()
    ll5.append(200)
    ll5.append(300)
    print("\nScenario 5: Before inserting at beginning, list is:")
    print(ll5)  # Expected: "200 -> 300"
    ll5.insert(0, 100)  # Insert 100 at index 0.
    print("After inserting 100 at index 0:")
    print(ll5)  # Expected: "100 -> 200 -> 300"

    # Scenario 6: Inserting at the end (index equals current length).
    ll6 = Linked_List()
    ll6.append(1)
    ll6.append(2)
    print("\nScenario 6: Before inserting at the end, list is:")
    print(ll6)  # Expected: "1 -> 2"
    ll6.insert(ll6.length, 3)  # Insert 3 at the last index.
    print("After inserting 3 at the last index:")
    print(ll6)  # Expected: "1 -> 2 -> 3"

    # Scenario 7: Attempt to insert at an invalid index.
    ll7 = Linked_List()
    ll7.append(5)
    ll7.append(10)
    print("\nScenario 7: Attempting to insert at an invalid index (-1):")
    result = ll7.insert(-1, 0)
    print("Insertion result (expected False):", result)  # Expected: False
    print("List remains unchanged:")
    print(ll7)  # Expected: "5 -> 10"

    # Scenario 8: Using a mix of operations
    ll8 = Linked_List()
    ll8.append(25)
    ll8.prepend(10)
    ll8.append(50)
    ll8.insert(2, 35)
    print("\nScenario 8: Mixed operations on the list:")
    print("After appending 25, prepending 10, appending 50, and inserting 35 at index 2:")
    print(ll8)  # Expected: "10 -> 25 -> 35 -> 50"
