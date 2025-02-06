# Node class to represent each element in the doubly linked list
class Node:
    def __init__(self, value):
        self.value = value  # Store the node's value
        self.next = None  # Pointer to the next node (default is None)
        self.prev = None  # Pointer to the previous node (default is None)


class DoublyLinkedList:
    """
    __init__:
    Initializes an empty doubly linked list.
    Attributes:
      - head: Points to the first node in the list.
      - tail: Points to the last node in the list.
      - length: Tracks the number of nodes in the list (initialized to 0).
    """

    def __init__(self):
        self.head = None  # No head node initially
        self.tail = None  # No tail node initially
        self.length = 0  # List is empty, so length is 0

    """
    __str__:
    Returns a string representation of the list.
    It traverses the list from head to tail and joins the node values with " <-> ".
    """

    def __str__(self):
        tempnode = self.head  # Start at the head of the list
        result = ''  # Initialize an empty string to build the representation
        while tempnode:
            result += str(tempnode.value)  # Append the current node's value
            if tempnode.next:
                result += " <-> "  # Add connector if there is a next node
            tempnode = tempnode.next  # Move to the next node
        return result  # Return the complete string

    """
    append:
    Inserts a new node with the given value at the end of the list.
    If the list is empty, the new node becomes both the head and tail.
    Otherwise, it links the new node after the current tail and updates the tail.
    """

    def append(self, value):
        newnode = Node(value)  # Create a new node with the given value
        if not self.head:  # If the list is empty
            self.head = newnode  # Set new node as the head
            self.tail = newnode  # Set new node as the tail
        else:
            self.tail.next = newnode  # Link the current tail's next to the new node
            newnode.prev = self.tail  # Set new node's previous to the current tail
            self.tail = newnode  # Update the tail to the new node
        self.length += 1  # Increment the list length

    """
    prepend:
    Inserts a new node with the given value at the beginning of the list.
    If the list is empty, the new node becomes both the head and tail.
    Otherwise, it links the new node before the current head and updates the head.
    """

    def prepend(self, value):
        newnode = Node(value)  # Create a new node with the given value
        if self.length == 0:  # If the list is empty
            self.head = newnode  # Set new node as head
            self.tail = newnode  # Set new node as tail
        else:
            newnode.next = self.head  # Link new node's next to current head
            self.head.prev = newnode  # Set current head's previous to new node
            self.head = newnode  # Update the head to the new node
        self.length += 1  # Increment the list length

    """
    traversal:
    Traverses the list from the head to the tail and prints each node's value.
    """

    def traversal(self):
        curr = self.head  # Start at the head
        while curr:
            print(curr.value)  # Print current node's value
            curr = curr.next  # Move to the next node

    """
    rev_traversal:
    Traverses the list from the tail to the head and prints each node's value.
    """

    def rev_traversal(self):
        last = self.tail  # Start at the tail
        while last:
            print(last.value)  # Print current node's value
            last = last.prev  # Move to the previous node

    """
    search:
    Searches for a node with the given target value in the list.
    Returns True if found; otherwise, returns False.
    """

    def search(self, target):
        curr = self.head  # Start at the head
        while curr:
            if curr.value == target:  # Compare each node's value with target
                return True  # Target found; return True
            curr = curr.next  # Move to the next node
        return False  # Target not found; return False

    """
    get:
    Retrieves the node at the specified index.
    Uses bidirectional traversal:
      - From head if index is in the first half.
      - From tail if index is in the second half.
    Returns the node if found; otherwise, returns None if index is out of bounds.
    """

    def get(self, index):
        if index < 0 or index >= self.length:
            return None  # Index out of bounds
        if index < self.length // 2:
            curr = self.head  # Start from head if index is in the first half
            for _ in range(index):
                curr = curr.next  # Move forward index times
        else:
            curr = self.tail  # Start from tail if index is in the second half
            for _ in range(self.length - 1, index, -1):
                curr = curr.prev  # Move backward until the target index
        return curr  # Return the found node

    """
    set:
    Updates the value of the node at the specified index.
    First, retrieves the node using get().
    If the node exists, updates its value and returns True.
    Otherwise, returns False.
    """

    def set(self, index, value):
        node = self.get(index)  # Retrieve node at the specified index
        if node:
            # Inline debug: print the current value before updating
            print("Before set:", node.value)  # Debug: shows old value
            node.value = value  # Update node's value
            return True  # Operation successful
        return False  # Node not found; operation failed

    """
    insert:
    Inserts a new node with the given value at the specified index.
    If the index is invalid, prints an error message and returns.
    For index 0, calls prepend; for an empty list, calls append.
    Otherwise, retrieves the node before the target index and adjusts pointers.
    """

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index Out of range")
            return  # Invalid index; exit function
        newnode = Node(value)  # Create the new node
        if index == 0:
            self.prepend(value)  # Insert at the beginning
            return
        elif self.length == 0:
            self.append(value)  # If the list is empty, append
            return
        temp_node = self.get(index - 1)  # Get node immediately before target index
        newnode.next = temp_node.next  # Set new node's next to current node at index
        newnode.prev = temp_node  # Set new node's previous to temp_node
        if temp_node.next:  # If there is a node after temp_node
            temp_node.next.prev = newnode  # Link that node's previous pointer to new node
        temp_node.next = newnode  # Link temp_node's next pointer to new node
        self.length += 1  # Increment list length

    """
    pop_first:
    Removes and returns the first node (head) of the list.
    If the list is empty, returns None.
    Otherwise, updates the head pointer to the next node and adjusts pointers.
    """

    def pop_first(self):
        if not self.head:
            return None  # List is empty; nothing to pop
        popped_node = self.head  # Store current head to return later
        if self.length == 1:
            self.head = None  # List becomes empty
            self.tail = None
        else:
            self.head = self.head.next  # Update head to the next node
            self.head.prev = None  # Remove backward link from new head
            popped_node.next = None  # Disconnect popped node from list
        self.length -= 1  # Decrement list length
        return popped_node  # Return the removed node

    """
    pop:
    Removes and returns the last node (tail) of the list.
    If the list is empty, returns None.
    Otherwise, updates the tail pointer to the previous node and adjusts pointers.
    """

    def pop(self):
        if not self.tail:
            return None  # List is empty; nothing to pop
        popped_node = self.tail  # Store current tail to return later
        if self.length == 1:
            self.head = None  # List becomes empty
            self.tail = None
        else:
            self.tail = self.tail.prev  # Update tail to the previous node
            self.tail.next = None  # Remove forward link from new tail
            popped_node.prev = None  # Disconnect popped node from list
        self.length -= 1  # Decrement list length
        return popped_node  # Return the removed node

    """
    remove:
    Removes and returns the node at the specified index.
    If the index is invalid, returns None.
    For index 0, calls pop_first; for the last index, calls pop.
    Otherwise, retrieves the node to be removed and adjusts the pointers of neighboring nodes.
    """

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None  # Index out of bounds; nothing to remove
        if index == 0:
            return self.pop_first()  # Remove the first node
        if index == self.length - 1:
            return self.pop()  # Remove the last node
        popped_node = self.get(index)  # Retrieve the node to be removed
        # Adjust pointers of adjacent nodes to bypass the removed node
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        # Disconnect the removed node completely
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1  # Decrement list length
        return popped_node  # Return the removed node


# ----------------------- TEST SCENARIOS BELOW -----------------------
if __name__ == '__main__':
    # Create a new DoublyLinkedList instance
    dll = DoublyLinkedList()

    print("Initial list (should be empty):")
    print(dll)  # Expected output: "" (empty string)

    # Scenario 1: Append nodes to the list
    print("\nScenario 1: Appending nodes")
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print("List after appending 10, 20, 30:")
    print(dll)  # Expected: "10 <-> 20 <-> 30"

    # Scenario 2: Prepend a node to the list
    print("\nScenario 2: Prepending a node")
    dll.prepend(5)
    print("List after prepending 5:")
    print(dll)  # Expected: "5 <-> 10 <-> 20 <-> 30"

    # Scenario 3: Traversal from head to tail
    print("\nScenario 3: Traversal (head to tail):")
    dll.traversal()  # Expected output (each value on a new line): 5, 10, 20, 30

    # Scenario 4: Reverse Traversal from tail to head
    print("\nScenario 4: Reverse Traversal (tail to head):")
    dll.rev_traversal()  # Expected output (each value on a new line): 30, 20, 10, 5

    # Scenario 5: Search for a value in the list
    print("\nScenario 5: Searching for a value")
    search_result = dll.search(20)
    print("Search for 20 (expected True):", search_result)
    search_result = dll.search(100)
    print("Search for 100 (expected False):", search_result)

    # Scenario 6: Get a node by index
    print("\nScenario 6: Get node at index 2")
    node = dll.get(2)
    if node:
        print("Node at index 2:", node.value)  # Expected: 20
    else:
        print("Index out of bounds")

    # Scenario 7: Set a node's value at a specific index
    print("\nScenario 7: Set node value at index 1")
    if dll.set(1, 15):
        print("After setting, list is:")
        print(dll)  # Expected: "5 <-> 15 <-> 20 <-> 30"
    else:
        print("Set operation failed.")

    # Scenario 8: Insert a node at a specific index
    print("\nScenario 8: Insert a node at index 2")
    dll.insert(2, 12)
    print("List after inserting 12 at index 2:")
    print(dll)  # Expected: "5 <-> 15 <-> 12 <-> 20 <-> 30"

    # Scenario 9: Pop the first node
    print("\nScenario 9: Pop the first node")
    popped_first = dll.pop_first()
    if popped_first:
        print("Popped first node value:", popped_first.value)  # Expected: 5
    print("List after popping first node:")
    print(dll)   #Expected : "15 <-> 12 <-> 20 <-> 30"

    # Scenario 10: Pop the last node
    print("\nScenario 10: Pop the last node")
    popped_last = dll.pop()
    if popped_last:
        print("Popped last node value:", popped_last.value)  # Expected: 30
    print("List after popping last node:")
    print(dll)    #Expected : "15 <-> 12 <-> 20"

    # Scenario 11: Remove a node from the middle of the list
    print("\nScenario 11: Remove node at index 1")
    removed_node = dll.remove(1)
    if removed_node:
        print("Removed node value:", removed_node.value)  #Removed node value: 12
    print("List after removal:")
    print(dll)        #Expected : "15  <-> 20"
