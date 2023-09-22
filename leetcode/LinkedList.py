from Node import Node
from typing import Optional


class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            initial_node = Node(data)
            self.head = initial_node
            self.tail = initial_node
            self.length = 1

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return True

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # 21. Merge Two Sorted Lists
    # https://leetcode.com/problems/merge-two-sorted-lists/
    """
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    
    Example 2:
    Input: list1 = [], list2 = []
    Output: []

    Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

    Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
    """

    def mergeTwoLists(
        self, list1: Optional[Node], list2: Optional[Node]
    ) -> Optional[Node]:
        dummy = Node(-1)
        current = dummy

        while list1 and list2:
            if list1.data < list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1

        if list2:
            current.next = list2

        return dummy.next

    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        # Iterative
        # current = head
        # prev = None

        # while current is not None:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node

        # return prev

        # recursive
        if head is None or head.next is None:
            return head

        reversed_sublist = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed_sublist
