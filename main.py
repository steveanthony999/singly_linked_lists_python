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
