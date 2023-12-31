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

        return True

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
        return current

    def prepend(self, value):
        """
        Prepends a new node with the given value to the start of the linked list.
        If the linked list is empty (i.e., the head is None), it sets the new node as both the head and tail.
        Otherwise, it sets the new node's next_node to the current head and updates the head to the new node.
        The length of the linked list is incremented by 1.
        """

        # Create a new node with the provided value.
        new_node = Node(value)

        # If the linked list is empty, set the new node as both the head and tail.
        if self.length == 0:
            self.tail = new_node
        # If the linked list is not empty, set the new node's next_node to the current head.
        else:
            new_node.next_node = self.head

        # Update the head to the new node.
        self.head = new_node

        # Increment the length of the linked list by 1.
        self.length += 1

        return True

    def pop_first(self):
        """
        Removes and returns the first node (head) of the linked list.

        If the linked list is empty, it returns None. If after removal, the list becomes empty,
        it updates the tail to None as well. The length of the linked list is decremented by 1.

        Returns:
            Node: The node that was removed. If the list is empty, returns None.
        """

        # If the linked list is empty, return None.
        if self.length == 0:
            return None

        # Store the current head node.
        current = self.head

        # Update the head to the next node.
        self.head = current.next_node

        # Detach the current node from the list.
        current.next_node = None

        # Decrement the length of the linked list by 1.
        self.length -= 1

        # If the list has become empty after removal, set the tail to None.
        if self.length == 0:
            self.tail = None

        # Return the removed node.
        return current

    def get(self, index):
        """
        Retrieves the node at the specified index in the linked list.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Node: The node at the specified index. If the index is out of bounds, returns None.
        """

        # Check if the index is out of bounds (negative or greater than or equal to the length of the list).
        # If so, return None.
        if index < 0 or index >= self.length:
            return None

        # Start at the head of the linked list.
        current = self.head

        # Traverse the linked list until reaching the desired index.
        for _ in range(index):
            current = current.next_node

        # Return the node at the specified index.
        return current

    def set_value(self, index, value):
        """
        Updates the value of the node at the specified index in the linked list.

        Args:
            index (int): The index of the node to update.
            value: The new value to set for the node at the specified index.

        Returns:
            bool: True if the value was successfully updated, False otherwise (e.g., if the index is out of bounds).
        """

        # Retrieve the node at the specified index using the get method.
        current = self.get(index)

        # If a node exists at the specified index, update its value.
        if current is not None:
            current.value = value
            return True

        # If the index is out of bounds or no node exists at the specified index, return False.
        return False

    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index in the linked list.

        Args:
            index (int): The index at which to insert the new node.
            value: The value for the new node.

        Returns:
            bool: True if the node was successfully inserted, False otherwise (e.g., if the index is out of bounds).
        """

        # Check if the index is out of bounds (either negative or greater than the length of the list).
        if index < 0 or index > self.length:
            return False

        # If the index is 0, prepend the new node to the start of the list.
        if index == 0:
            return self.prepend(value)

        # If the index is equal to the length of the list, append the new node to the end of the list.
        if index == self.length:
            return self.append(value)

        # Create a new node with the given value.
        new_node = Node(value)

        # Retrieve the node immediately before the specified index.
        temp = self.get(index - 1)

        # Set the next_node of the new node to point to the node that currently occupies the specified index.
        new_node.next_node = temp.next_node

        # Update the next_node of the node immediately before the specified index to point to the new node.
        temp.next_node = new_node

        # Increment the length of the linked list.
        self.length += 1

        # Return True to indicate successful insertion.
        return True

    def remove(self, index):
        """
        Removes a node at the specified index from the linked list.

        If the index is out of bounds, the method returns None.
        If the index points to the first node, it uses the pop_first method.
        If the index points to the last node, it uses the pop method.
        For any other index, it updates the references to remove the target node
        and decrements the list's length.

        Args:
        - index (int): The position of the node to be removed.

        Returns:
        - Node: The removed node. Returns None if the index is out of bounds.
        """

        # Check if the index is out of bounds of the linked list.
        if index < 0 or index >= self.length:
            return None

        # If the index is 0, remove the first node.
        if index == 0:
            return self.pop_first()

        # If the index is the last position, remove the last node.
        if index == self.length - 1:
            return self.pop()

        # Get the node just before the target node to be removed.
        prev_node = self.get(index - 1)

        # Get the target node to be removed.
        current = prev_node.next_node

        # Update the 'next_node' reference of the previous node to skip the target node.
        prev_node.next_node = current.next_node

        # Clear the 'next_node' reference of the target node.
        current.next_node = None

        # Decrement the length of the linked list.
        self.length -= 1

        # Return the removed node.
        return current

    def reverse(self):
        """
        Reverses the linked list in-place.

        This method iterates through the linked list and modifies the next_node pointers of each node
        to point to the previous node, effectively reversing the list. After the reversal, the head
        and tail pointers of the linked list are updated accordingly.
        """

        # Start at the head of the linked list.
        current = self.head

        # Update the head to point to the current tail and the tail to point to the current head.
        self.head = self.tail
        self.tail = current

        # Initialize pointers to keep track of the next node and the previous node.
        after_node = current.next_node
        prev_node = None

        # Iterate through the linked list.
        for _ in range(self.length):
            # Store the next node before modifying the current node's next_node pointer.
            after_node = current.next_node

            # Update the current node's next_node pointer to point to the previous node.
            current.next_node = prev_node

            # Move to the next node in the original sequence.
            prev_node = current
            current = after_node

    def find_middle_node(self):
        """
        Finds and returns the middle node of the linked list.

        This method uses the two-pointer technique: a slow pointer and a fast pointer.
        The slow pointer moves one step at a time, while the fast pointer moves two steps.
        By the time the fast pointer reaches the end of the list, the slow pointer will be at the middle.

        If the linked list has an even number of nodes, this method returns the second middle node.
        For example, in the list [1, 2, 3, 4], it will return the node with value 3.

        Returns:
            Node: The middle node of the linked list. If the list is empty, returns None.
        """

        # Initialize the slow and fast pointers to the head of the linked list.
        slow = self.head
        fast = self.head

        # Traverse the linked list with the fast pointer moving twice as fast as the slow pointer.
        while fast is not None and fast.next_node is not None:
            slow = slow.next_node  # Move the slow pointer one step.
            fast = fast.next_node.next_node  # Move the fast pointer two steps.

        # When the loop ends, the slow pointer will be at the middle of the linked list.
        return slow

    def has_loop(self):
        """
        Determines if the linked list contains a loop/cycle using Floyd's Cycle-Finding Algorithm.

        This algorithm, also known as the "Tortoise and the Hare" algorithm, uses two pointers that move through
        the list at different speeds. The slow pointer ('tortoise') moves one step at a time while the fast pointer
        ('hare') moves two steps at a time. If there is a loop in the list, the fast pointer will eventually catch up
        to the slow pointer. If there's no loop, the fast pointer will reach the end of the list.

        Returns:
            bool: True if the linked list has a loop, False otherwise.
        """

        # Initialize two pointers: 'slow' and 'fast'. Both start at the head of the linked list.
        slow = self.head
        fast = self.head

        # Continue the loop as long as the 'fast' pointer is not None and its next node is also not None.
        while fast is not None and fast.next_node is not None:
            # Move the 'slow' pointer one step/node at a time.
            slow = slow.next_node
            # Move the 'fast' pointer two steps/nodes at a time.
            fast = fast.next_node.next_node

            # If the 'fast' pointer catches up to the 'slow' pointer, it means there's a loop in the linked list.
            if fast == slow:
                return True

        # If the loop completes without the 'fast' pointer catching up to the 'slow' pointer, there's no loop.
        return False

    def empty_linked_list(self):
        """
        Empties the linked list by setting the head and tail to None and the length to 0.

        This method effectively removes all nodes from the linked list, making it an empty list.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):
        """
        Partition the linked list such that all nodes with values less than x come
        before nodes with values greater than or equal to x, while preserving the
        original relative order of the nodes in each of the two partitions.

        Args:
        - x (int): The partitioning value.

        Returns:
        None: The function modifies the linked list in place.
        """

        # Check if the list is empty
        if self.head is None:
            return None

        # Initialize dummy nodes to assist in partitioning
        dummy1 = Node(0)
        dummy2 = Node(0)

        # Set pointers to the start of the two new partitions
        prev1 = dummy1
        prev2 = dummy2

        # Start traversal from the head of the list
        current = self.head

        # Traverse the list and partition nodes based on their value relative to x
        while current is not None:
            if current.value < x:
                prev1.next_node = current
                prev1 = current
            else:
                prev2.next_node = current
                prev2 = current
            current = current.next_node

        # Terminate the two partitions
        prev1.next_node = None
        prev2.next_node = None

        # Connect the two partitions
        prev1.next_node = dummy2.next_node

        # Update the head to point to the start of the partitioned list
        self.head = dummy1.next_node

    def remove_duplicates(self):
        """
        Removes duplicate nodes from the linked list.

        This method traverses the linked list and uses a set to keep track of
        the values that have been encountered. If a duplicate value is found,
        the node containing that value is removed from the list. The relative
        order of the remaining nodes is preserved.

        Attributes:
            self (LinkedList): The linked list from which duplicates are to be removed.

        Returns:
            None: The method modifies the linked list in-place and does not return any value.
        """

        # Initialize a set to store unique values from the linked list
        values = set()

        # Initialize pointers for the previous and current nodes
        prev = None
        current = self.head

        # Traverse the linked list
        while current is not None:
            # If the current value is already in the set (i.e., it's a duplicate)
            if current.value in values:
                # Bypass the current node to remove it from the list
                prev.next_node = current.next_node
                # Decrement the length of the linked list
                self.length -= 1
            else:
                # If the value is unique, add it to the set
                values.add(current.value)
                # Move the previous pointer to the current node
                prev = current

            # Move to the next node in the list
            current = current.next_node

    def binary_to_decimal(self):
        """
        Convert a binary number represented by a linked list to its decimal equivalent.

        The linked list represents a binary number where each node contains a single bit (0 or 1).
        The head of the linked list represents the least significant bit (LSB), and the tail
        represents the most significant bit (MSB).

        Returns:
            int: The decimal representation of the binary number.
        """

        # Initialize the decimal value to 0
        decimal = 0

        # Start at the head of the linked list
        current = self.head

        # Traverse the linked list
        while current is not None:
            # For each bit, shift the current decimal value to the left (multiply by 2)
            # and add the current bit's value
            decimal = decimal * 2 + current.value

            # Move to the next node
            current = current.next_node

        # Return the final decimal value
        return decimal

    def reverse_between(self, m, n):
        """
        Reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.

        Parameters:
        - m (int): The starting index for the reverse.
        - n (int): The ending index for the reverse.

        Returns:
        None: If the linked list is empty or has only one node.
        Otherwise, it modifies the linked list in-place.

        Example:
        Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4.
        After calling this method, the linked list will be modified to 1 -> 2 -> 5 -> 4 -> 3.
        """

        # If the linked list has only one node or is empty
        if self.length <= 1:
            return None

        # Initialize a dummy node
        dummy = Node(0)
        dummy.next_node = self.head
        prev = dummy

        # Move the prev pointer to the node just before the m-th node
        for _ in range(m):
            prev = prev.next_node

        # Set current to the m-th node
        current = prev.next_node

        # Reverse the nodes between m and n
        for _ in range(n - m):
            node_to_move = current.next_node
            current.next_node = node_to_move.next_node
            node_to_move.next_node = prev.next_node
            prev.next_node = node_to_move

        # Update the head of the linked list
        self.head = dummy.next_node

    def merge_two_lists(self, list1, list2):
        """
        Merge two sorted linked lists into a single sorted linked list.

        Parameters:
        - list1: Head of the first sorted linked list.
        - list2: Head of the second sorted linked list.

        Returns:
        - Head of the merged sorted linked list.
        """

        # Initialize a dummy node to simplify the merging process
        dummy = Node(-1)
        # 'current' will be used to traverse and build the merged list
        current = dummy

        # Continue until one of the lists becomes empty
        while list1 and list2:
            # If the current node of list1 has a smaller value
            if list1.value < list2.value:
                # Attach list1's node to the merged list
                current.next_node = list1
                # Move to the next node in list1
                list1 = list1.next_node
            else:
                # Attach list2's node to the merged list
                current.next_node = list2
                # Move to the next node in list2
                list2 = list2.next_node
            # Move to the next position in the merged list
            current = current.next_node

        # If list1 is not empty, attach its remaining nodes to the merged list
        if list1:
            current.next_node = list1
        # If list2 is not empty, attach its remaining nodes to the merged list
        if list2:
            current.next_node = list2

        # Return the head of the merged list (next of the dummy node)
        return dummy.next_node

    def merge_two_lists_recursively(self, list1, list2):
        """
        Merge two sorted linked lists into one sorted linked list using recursion.

        Parameters:
        - list1: The head node of the first sorted linked list.
        - list2: The head node of the second sorted linked list.

        Returns:
        - The head node of the merged sorted linked list.

        Example:
        If list1 is 1 -> 2 -> 4 and list2 is 1 -> 3 -> 4,
        the merged list will be 1 -> 1 -> 2 -> 3 -> 4 -> 4.
        """

        # Base cases: if one of the lists is empty, return the other list.
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Determine which node has a smaller value and set it as the current head.
        if list1.value < list2.value:
            head = list1
            list1 = list1.next_node
        else:
            head = list2
            list2 = list2.next_node

        # Recursively merge the remaining nodes and link them to the current head.
        head.next_node = self.merge_two_lists_recursively(list1, list2)

        return head


def find_kth_from_end(ll, k):
    """
    Returns the k-th node from the end of a linked list.

    This function uses the two-pointer technique to efficiently find the k-th node
    from the end of the linked list in a single pass without needing to know the length
    of the list. The fast pointer moves k nodes ahead first. If the list has fewer than
    k nodes, it returns None. Otherwise, both pointers move forward until the fast
    pointer reaches the end. The slow pointer will then be at the k-th position from the end.

    Args:
        ll (LinkedList): The linked list to search.
        k (int): The position from the end to retrieve.

    Returns:
        Node: The k-th node from the end, or None if the list has fewer than k nodes.
    """

    # Initialize both pointers to the head of the linked list.
    slow = ll.head
    fast = ll.head

    # Move the fast pointer k nodes ahead.
    for _ in range(k):
        # If the fast pointer reaches the end before moving k nodes, return None.
        if fast is None:
            return None
        fast = fast.next_node

    # Move both pointers at the same pace until the fast pointer reaches the end.
    while fast is not None:
        slow = slow.next_node
        fast = fast.next_node

    # Return the slow pointer, which is now at the k-th position from the end.
    return slow


# append
my_linked_list = LinkedList(69)
my_linked_list.append(420)
my_linked_list.append(999)
my_linked_list.print_list()
print("-------------------")

# pop
pop_node = my_linked_list.pop()
print(pop_node)
print("-------------------")

# prepend
my_linked_list.prepend(1)
my_linked_list.print_list()
print("-------------------")

# pop_first
pop_first_node = my_linked_list.pop_first()
print(pop_first_node.value)
print("-------------------")

# get
get_index_at_one = my_linked_list.get(1)
print(get_index_at_one.value)
print("-------------------")

# set_value
my_linked_list.print_list()
set_value_at_index = my_linked_list.set_value(1, 25)
my_linked_list.print_list()
print(set_value_at_index)
print("-------------------")

# insert
my_linked_list.print_list()
my_linked_list.insert(1, 600)
my_linked_list.print_list()
print("-------------------")

# remove
my_linked_list.remove(1)
my_linked_list.print_list()
print("-------------------")

# reverse
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
print("-------------------")

# find_middle_node
my_linked_list.remove(0)
my_linked_list.remove(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
print(my_linked_list.find_middle_node().value)
print("-------------------")

# find_kth_from_end
k = 2
result = find_kth_from_end(my_linked_list, k)
print(result.value)  # Output: 4
print("-------------------")

# partition_list
my_linked_list.empty_linked_list()
my_linked_list.append(2)
my_linked_list.append(8)
my_linked_list.append(1)
my_linked_list.append(4)
my_linked_list.append(3)
my_linked_list.append(7)
my_linked_list.partition_list(4)
my_linked_list.print_list()
print("-------------------")

# remove_duplicates
my_linked_list.empty_linked_list()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(1)
my_linked_list.append(4)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.remove_duplicates()
my_linked_list.print_list()
print("-------------------")

# binary_to_decimal
my_linked_list.empty_linked_list()
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.print_list()
print(my_linked_list.binary_to_decimal())
print("-------------------")

# reverse_between
my_linked_list.empty_linked_list()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.reverse_between(2, 4)
my_linked_list.print_list()
print("-------------------")

# merge_two_lists
my_linked_list.empty_linked_list()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
my_merged_linked_list = my_linked_list.merge_two_lists(
    my_linked_list.head, my_linked_list_2.head
)
while my_merged_linked_list is not None:
    print(my_merged_linked_list.value)
    my_merged_linked_list = my_merged_linked_list.next_node
print("-------------------")

my_linked_list.empty_linked_list()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(3)
my_linked_list_2.append(4)

merged_list = my_linked_list.merge_two_lists_recursively(
    my_linked_list.head, my_linked_list_2.head
)

while merged_list is not None:
    print(merged_list.value)
    merged_list = merged_list.next_node
print("-------------------")
