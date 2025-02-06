# CREATION

"""
We can implement a Stack using Python list.

Advantages:
  - Easy to implement.
  - Provides basic stack operations like push, pop, peek, and check for emptiness.

Disadvantages:
  - May have speed issues as the size of the stack grows.
"""


class Stack:
    """
    __init__:
    Initializes an empty stack.

    Attributes:
      list: A Python list used to store stack elements.
    """
    def __init__(self):
        self.list = []  # Start with an empty list representing the stack

        """
        __str__:
        Returns a string representation of the stack.

        The elements are shown in LIFO order (top of the stack first).
        """

    def __str__(self):
        # Reverse the list so that the top of the stack is shown first
        values = [str(x) for x in reversed(self.list)]
        # Join the values with a newline separator for a clear view
        return '\n'.join(values)

    """
        isEmpty:
        Checks if the stack is empty.

        Returns:
          True if the stack is empty; otherwise, returns False.
    """

    def isEmpty(self):
        # Check if the list is empty
        if self.list == []:
            return True
        else:
            return False

    """
        push:
        Adds a new element to the top of the stack.

        Parameters:
          value: The element to be pushed onto the stack.

        Returns:
          A confirmation message indicating that the element was successfully inserted.
     """
    def push(self, value):
        self.list.append(value)  # Append the new element to the end of the list
        return "The element has been successfully inserted"



    """
        pop:
        Removes and returns the top element of the stack.

        Returns:
          The popped element if the stack is not empty; otherwise, an error message.
     """
    def pop(self):

        # Check if the stack is empty before trying to pop an element
        if self.isEmpty():
            return "There is no item in the stack"
        else:
            return self.list.pop()  # Remove and return the last element from the list


    """
        peek:
        Returns the top element of the stack without removing it.

        Returns:
          The top element if the stack is not empty; otherwise, an error message.
    """
    def peek(self):

        # Check if the stack is empty
        if self.isEmpty():
            return "There is no item in the stack"
        else:
            # Return the last element which is at the top of the stack
            return self.list[len(self.list) - 1]

    """
            delete:
            Deletes the entire stack by removing the reference to the list.

            After calling this method, the stack will be set to None.
            """
    def delete(self):

        self.list = None  # Remove the list, effectively deleting the stack


# ----------------------- TEST CODE BELOW -----------------------
# The following code demonstrates the stack functionality with various scenarios.

if __name__ == '__main__':
    # Create a new stack instance
    customStack = Stack()

    # Scenario 1: Check if the stack is empty
    print("Scenario 1: Check if the stack is empty")
    print("Is stack empty?", customStack.isEmpty())  # Expected output: True

    # Scenario 2: Push elements onto the stack
    print("\nScenario 2: Push elements onto the stack")
    print(customStack.push(10))  # Expected: Confirmation message
    print(customStack.push(20))  # Expected: Confirmation message
    print(customStack.push(30))  # Expected: Confirmation message

    # Print the current stack
    print("\nCurrent stack (top element first):")
    print(customStack)
    # Expected output (top to bottom):
    # 30
    # 20
    # 10

    # Scenario 3: Peek at the top element of the stack
    print("\nScenario 3: Peek at the top element")
    print("Top element is:", customStack.peek())  # Expected: 30

    # Scenario 4: Pop an element from the stack
    print("\nScenario 4: Pop an element from the stack")
    popped_item = customStack.pop()
    print("Popped element is:", popped_item)  # Expected: 30

    # Print the current stack after pop
    print("Stack after popping one element:")
    print(customStack)
    # Expected output (top to bottom):
    # 20
    # 10

    # Scenario 5: Check if the stack is empty after popping
    print("\nScenario 5: Check if the stack is empty after popping elements")
    print("Is stack empty?", customStack.isEmpty())  # Expected output: False

    # Scenario 6: Delete the entire stack
    print("\nScenario 6: Delete the entire stack")
    customStack.delete()
    # Trying to print the stack after deletion; it should show None
    print("Stack after deletion:", customStack.list)
