# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # initialize dummy node to *land* the slow pointer onto the node before the node to be removed
        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy

        # move the fast pointer n times ahead of the slow pointer
        # this allows a constant offset of n spaces to help us know when
        # we are n spaces from the end of the list
        for _ in range(n):
            fast = fast.next

        # move the fast pointer to the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # this simply jumps the nth node of the linked list to
        # remove it from the linked list
        slow.next = slow.next.next

        return dummy.next
