f"""
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.
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
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# list1 = [ListNode(1), ListNode(1), ListNode(2), ListNode(3), ]
# list2 = [ListNode(0), ListNode(3), ListNode(4), ListNode(5), ]

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                            list2: Optional[ListNode]) -> Optional[ListNode]:
        first = pointer = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                pointer, list1 = list1, list1.next
            else:
                pointer.next = list2
                pointer, list2 = list2, list2.next

        if list1 or list2:
            pointer.next = list1 if list1 else list2

        return first.next
