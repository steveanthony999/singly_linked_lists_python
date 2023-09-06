# A Node represents a single element in a singly linked list.
# It contains data (the value of the element) and a reference to the next node in the sequence.
# If the next reference is None, it indicates the end of the list.


# Define the Node class to represent individual elements in a linked list.
class Node:
    # Constructor for the Node class.
    # Initializes a node with a given value and an optional reference to the next node.
    # If no next node is provided, it defaults to None, indicating the end of the list.
    def __init__(self, value, next_node=None):
        # The data value stored in the node.
        self.value = value
        # Reference to the next node in the linked list.
        self.next_node = next_node


# A singly linked list is a data structure that consists of nodes.
# Each node holds a value and a reference (or link) to the next node in the sequence.
# The list is called 'singly linked' because each node points only to the next node,
# and there's no backward traversal. The start of the list is referred to as the 'head',
# and the end of the list (where the next node is None) is the 'tail'.


class LinkedList:
    """
    Represents a singly linked list. A linked list is a linear data structure
    where each element is a separate object called a node. Each node contains
    a value and a reference (or link) to the next node in the sequence.
    """

    def __init__(self, value=None):
        """
        Initializes a linked list.

        If an initial value is provided, the linked list starts with one node
        containing that value. Otherwise, the linked list is initialized empty.

        Args:
        - value (optional): The initial value for the linked list.
        """
        if value is None:
            # Indicate the start of the linked list. None means the list is empty.
            self.head = None
            # Indicate the end of the linked list. None means the list is empty.
            self.tail = None
            # Represent the number of nodes in the linked list.
            self.length = 0
        else:
            # Create a new node with the provided value.
            initial_node = Node(value)
            # Set the new node as the starting node of the linked list.
            self.head = initial_node
            # Set the new node as the ending node of the linked list.
            self.tail = initial_node
            # Set the number of nodes in the linked list to 1.
            self.length = 1

    def print_list(self):
        """
        Traverse the linked list and print the value of each node.
        This method provides a visual representation of the linked list's contents.
        """
        # Start at the head of the linked list.
        current = self.head

        # Traverse the linked list until reaching the end.
        while current is not None:
            # Print the value of the current node.
            print(current.value)

            # Move to the next node in the list.
            current = current.next_node

    def append(self, value):
        """
        Appends a new node with the given value to the end of the linked list.
        If the linked list is empty (i.e., the head is None), it sets the new node as the head.
        Otherwise, it attaches the new node to the tail's next_node and updates the tail to the new node.
        The length of the linked list is incremented by 1.
        """
        # Create a new node with the provided value.
        new_node = Node(value)

        # If the linked list is empty, set the new node as the head.
        if self.head is None:
            self.head = new_node
        # If the linked list is not empty, attach the new node to the tail's next_node.
        else:
            self.tail.next_node = new_node

        # Update the tail to the new node.
        self.tail = new_node

        # Increment the length of the linked list by 1.
        self.length += 1

    def pop(self):
        """
        Removes and returns the value of the last node in the linked list.
        If the linked list is empty, it returns None.
        """

        # If the linked list is empty, return None.
        if self.length == 0:
            return None

        # If there's only one node in the linked list.
        if self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return value

        # Start at the head of the linked list.
        current = self.head
        # This will be the node before the last node (the one we want to remove).
        previous = None

        # Traverse the linked list until reaching the last node.
        while current.next_node is not None:
            previous = current
            current = current.next_node

        # Set the node before the last node as the new tail.
        self.tail = previous
        # The new tail's next_node should be None since it's now the last node.
        self.tail.next_node = None
        # Decrement the length of the linked list by 1.
        self.length -= 1

        # Return the value of the removed node.
        return current.value


my_linked_list = LinkedList(69)
my_linked_list.append(420)
my_linked_list.append(999)

my_linked_list.print_list()

print(my_linked_list.pop())

my_linked_list.print_list()
