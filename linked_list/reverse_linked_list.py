from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # initialize None for last node

        while head:
            curr = head         # make a temp pointer CURR to head
            head = head.next    # go to head.next
            curr.next = prev    # make CURR point to the PREV node
            prev = curr         # set PREV as CURR ndoe

        return prev

    def recursiveReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head, prev=None):
            if not head:
                return prev

            nxt = head.next
            head.next = prev

            return helper(nxt, head)

        return helper(head)
