# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SlowSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedList = None

        for lst in lists:
            mergedList = self.mergeSortedLists(mergedList, lst)

        return mergedList

    def mergeSortedLists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class DivideAndConquerSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists) // 2
            l = self.mergeKLists(lists[:mid])
            r = self.mergeKLists(lists[mid:])

            return self.mergeSortedLists(l, r)

    def mergeSortedLists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next

