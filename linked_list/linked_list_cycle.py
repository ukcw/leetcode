# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # this method uses two pointers
        # one fast moving pointer that moves two times
        # one slow moving pointer that moves one time
        # they start at the same head position
        slow = fast = head

        # since the fast pointer moves two steps each time
        # case 1: it hits the NULL pointer at the end of a linked list,
        #         if this is the case, then the first condition captures it.
        # case 2: it hits the node before the NULL pointer at the end of the
        #         linked list, if this is the case, then the second condition
        #         captures this.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # if the linked list has a cycle, then at some point, the fast
            # moving pointer will catch up to the slow pointer within the
            # cycle. Since the fast moving pointer moves two steps for each
            # single step taken by the slow pointer, the fast pointer will be
            # n steps ahead of the slow pointer when it enters the cycle, given
            # that the cycle only starts after n nodes in the linked list.
            # Additionally, on each iteration, the fast pointer will close up
            # the distance on the slow pointer by one step, this means that it
            # will take [cycle_length % n] steps to be at the same position as
            # the slow pointer.
            if slow == fast:
                return True

        return False
