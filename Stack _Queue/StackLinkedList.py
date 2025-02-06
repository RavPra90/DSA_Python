"""
We can implement a Stack using a Python Linked List.

Advantages:
  - Fast Performance
  - Provides basic stack operations like push, pop, peek, and check for emptiness.

Disadvantages:
  - Tougher to implement compared to using a Python list
"""

# Node class for the linked list
class Node:
    """
           Initializes a new node with the provided value.

           Parameters:
             value: The value to be stored in the node (default is None).

           Attributes:
             value: Stores the given value.
             next: Pointer to the next node (initially None).
        """
    def __init__(self, value=None):

        self.value = value          # Store the given value in the node
        self.next = None            # Pointer to the next node; initially there is no next node

# LinkedList class to support the Stack implementation
class LinkedList:
    """
            Initializes an empty linked list.

            Attributes:
              head: Points to the first node in the list (None if the list is empty).
            """
    def __init__(self):
        self.head = None            # Initially, the list is empty

        """
        Makes the linked list iterable.

        Yields:
          Each node in the linked list sequentially.
        """
    def __iter__(self):
        curNode = self.head         # Start at the head node
        while curNode:
            yield curNode           # Yield the current node
            curNode = curNode.next  # Move to the next node


# Stack class implemented using a linked list
class Stack:
    """
    Initializes an empty stack using a linked list.

    Attributes:
      LinkedList: An instance of LinkedList to store stack elements.
    """
    def __init__(self):
        self.LinkedList = LinkedList()  # Create a new empty linked list for the stack

        """
        Returns a string representation of the stack.

        The elements are displayed from top (head) to bottom.
        """
    def __str__(self):
        # Create a list of string values for each node in the linked list (top to bottom)
        values = [str(node.value) for node in self.LinkedList]
        # Join the values with a newline separator for a clear view
        return '\n'.join(values)

    """
        Checks whether the stack is empty.

        Returns:
          True if the stack is empty; otherwise, False.
        """
    def isEmpty(self):

        # The stack is empty if the head of the linked list is None
        if self.LinkedList.head is None:
            return True
        else:
            return False


    """
        Pushes a new element onto the top of the stack.

        Parameters:
          value: The element to be added to the stack.

        Process:
          - Create a new node with the provided value.
          - Set its next pointer to the current head.
          - Update the head of the linked list to this new node.
        """
    def push(self, value):
        node = Node(value)                    # Create a new node with the provided value
        node.next = self.LinkedList.head      # Link new node's next to the current head (top of stack)
        self.LinkedList.head = node           # Update the head to the new node


        """
        Removes and returns the top element from the stack.

        Returns:
          The value of the popped element if the stack is not empty; otherwise, an error message.

        Process:
          - If the stack is empty, return an error message.
          - Otherwise, retrieve the value from the head node.
          - Update the head pointer to the next node.
        """
    def pop(self):

        if self.isEmpty():
            return "There are no elements in the Stack"
        else:
            nodeValue = self.LinkedList.head.value  # Retrieve the top element's value
            self.LinkedList.head = self.LinkedList.head.next  # Update the head to the next node
            return nodeValue                         # Return the popped element's value


    """
        Returns the top element of the stack without removing it.

        Returns:
          The value of the top element if the stack is not empty; otherwise, an error message.
        """
    def peek(self):
        if self.isEmpty():
            return "There are no elements in the Stack"
        else:
            return self.LinkedList.head.value       # Return the value at the top of the stack

    """
        Deletes the entire stack by resetting the linked list.

        Process:
          - Set the head of the linked list to None.
        """
    def delete(self):
        self.LinkedList.head = None                  # Delete the stack by removing the head reference




# ----------------------- TEST CODE BELOW -----------------------
# The following test scenarios demonstrate the functionality of the stack implemented using a linked list.

if __name__ == '__main__':
    # Create a new stack instance
    customStack = Stack()

    # Scenario 1: Check if the stack is empty
    print("Scenario 1: Check if the stack is empty")
    print("Is stack empty?", customStack.isEmpty())  # Expected output: True

    # Scenario 2: Push elements onto the stack
    print("\nScenario 2: Push elements onto the stack")
    customStack.push(10)
    customStack.push(20)
    customStack.push(30)
    print("Stack after pushing 10, 20, 30:")
    print(customStack)
    # Expected output (top element first):
    # 30
    # 20
    # 10

    # Scenario 3: Peek at the top element of the stack
    print("\nScenario 3: Peek at the top element")
    print("Top element is:", customStack.peek())  # Expected output: 30

    # Scenario 4: Pop an element from the stack
    print("\nScenario 4: Pop an element from the stack")
    popped_item = customStack.pop()
    print("Popped element is:", popped_item)  # Expected output: 30

    # Print the current stack after pop
    print("Stack after popping one element:")
    print(customStack)
    # Expected output (top element first):
    # 20
    # 10

    # Scenario 5: Check if the stack is empty after popping elements
    print("\nScenario 5: Check if the stack is empty after popping elements")
    print("Is stack empty?", customStack.isEmpty())  # Expected output: False

    # Scenario 6: Delete the entire stack
    print("\nScenario 6: Delete the entire stack")
    customStack.delete()
    # After deletion, printing the stack should yield an empty output
    print("Stack after deletion:")
    print(customStack)  # Expected output: (empty string)
