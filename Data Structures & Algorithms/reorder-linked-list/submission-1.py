# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find middle with slow/fast pointers
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the second half
        #   - seperate 2nd half of list
        second = slow.next
        slow.next = None
        #   - reverse 2nd half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # 3. merge the two halves
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2