# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use two pointers
        # find the middle point of the linked list
        # split the first, and second section of the list
        # if the list has an even length, then the middle point would be node number len(linked_list) // 2
        # if odd length, then the middle point will be node number len(linked_list) // 2 + 1
        # in either case, it is okay because the middle point (also the last node of the first section)
        # will be the node that we want to be in last position in the final resulting linked list.

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next

        # once we have split the first and second sections of the list
        # we reverse the second section of the list

        prev = slow.next = None

        while second:
            curr = second.next
            second.next = prev
            prev = second
            second = curr

        # this provides us with the necessary pointers and direction to then go on and merge
        # the first and second sections of the list in the required order

        start = head
        second = prev

        while second:
            # save next node
            # point current node to node in second section
            # save next node
            currFirst = head.next
            head.next = second
            head = currFirst

            currSecond = second.next
            second.next = head
            second = currSecond

            # a more elegant way of doing the merge
            # nextt = head.next
            # head.next = second
            # head = second
            # second = nextt
        return start
