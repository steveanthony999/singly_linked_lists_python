class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            initial_node = Node(value)
            self.head = initial_node
            self.tail = initial_node
            self.length = 1

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.value)

            current = current.next_node

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node

        self.tail = new_node

        self.length += 1

        return True

    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return value

        current = self.head
        previous = None

        while current.next_node is not None:
            previous = current
            current = current.next_node

        self.tail = previous
        self.tail.next_node = None
        self.length -= 1

        return current

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.tail = new_node
        else:
            new_node.next_node = self.head

        self.head = new_node

        self.length += 1

        return True

    def pop_first(self):
        if self.length == 0:
            return None

        current = self.head

        self.head = current.next_node

        current.next_node = None

        self.length -= 1

        if self.length == 0:
            self.tail = None

        return current

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        current = self.head

        for _ in range(index):
            current = current.next_node

        return current

    def set_value(self, index, value):
        current = self.get(index)

        if current is not None:
            current.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)

        temp = self.get(index - 1)

        new_node.next_node = temp.next_node

        temp.next_node = new_node

        self.length += 1

        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        prev_node = self.get(index - 1)

        current = prev_node.next_node

        prev_node.next_node = current.next_node

        current.next_node = None

        self.length -= 1

        return current

    def reverse(self):
        current = self.head

        self.head = self.tail
        self.tail = current

        after_node = current.next_node
        prev_node = None

        for _ in range(self.length):
            after_node = current.next_node

            current.next_node = prev_node

            prev_node = current
            current = after_node

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node

        return slow

    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node

            if fast == slow:
                return True

        return False

    def empty_linked_list(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):
        if self.head is None:
            return None

        dummy1 = Node(0)
        dummy2 = Node(0)

        prev1 = dummy1
        prev2 = dummy2

        current = self.head

        while current is not None:
            if current.value < x:
                prev1.next_node = current
                prev1 = current
            else:
                prev2.next_node = current
                prev2 = current
            current = current.next_node

        prev1.next_node = None
        prev2.next_node = None

        prev1.next_node = dummy2.next_node

        self.head = dummy1.next_node

    def remove_duplicates(self):
        values = set()

        prev = None
        current = self.head

        while current is not None:
            if current.value in values:
                prev.next_node = current.next_node
                self.length -= 1
            else:
                values.add(current.value)
                prev = current

            current = current.next_node

    def binary_to_decimal(self):
        decimal = 0

        current = self.head

        while current is not None:
            decimal = decimal * 2 + current.value

            current = current.next_node

        return decimal

    def reverse_between(self, m, n):
        if self.length <= 1:
            return None

        dummy = Node(0)
        dummy.next_node = self.head
        prev = dummy

        for _ in range(m):
            prev = prev.next_node

        current = prev.next_node

        for _ in range(n - m):
            node_to_move = current.next_node
            current.next_node = node_to_move.next_node
            node_to_move.next_node = prev.next_node
            prev.next_node = node_to_move

        self.head = dummy.next_node


def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next_node

    while fast is not None:
        slow = slow.next_node
        fast = fast.next_node

    return slow


my_linked_list = LinkedList(69)
my_linked_list.append(420)
my_linked_list.append(999)
my_linked_list.print_list()
print("-------------------")

pop_node = my_linked_list.pop()
print(pop_node)
print("-------------------")

my_linked_list.prepend(1)
my_linked_list.print_list()
print("-------------------")

pop_first_node = my_linked_list.pop_first()
print(pop_first_node.value)
print("-------------------")

get_index_at_one = my_linked_list.get(1)
print(get_index_at_one.value)
print("-------------------")

my_linked_list.print_list()
set_value_at_index = my_linked_list.set_value(1, 25)
my_linked_list.print_list()
print(set_value_at_index)
print("-------------------")

my_linked_list.print_list()
my_linked_list.insert(1, 600)
my_linked_list.print_list()
print("-------------------")

my_linked_list.remove(1)
my_linked_list.print_list()
print("-------------------")

my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
print("-------------------")

my_linked_list.remove(0)
my_linked_list.remove(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
print(my_linked_list.find_middle_node().value)
print("-------------------")

k = 2
result = find_kth_from_end(my_linked_list, k)
print(result.value)  # Output: 4
print("-------------------")


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

my_linked_list.empty_linked_list()
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.print_list()
print(my_linked_list.binary_to_decimal())
print("-------------------")

my_linked_list.empty_linked_list()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.reverse_between(2, 4)
my_linked_list.print_list()
print("-------------------")
