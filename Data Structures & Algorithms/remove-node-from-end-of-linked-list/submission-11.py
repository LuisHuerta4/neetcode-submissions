# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        if head.next == None:
            return None

        size = 0
        while head:
            size += 1
            head = head.next
        
        head = start
        if size == 2:
            if n == 1:
                head.next = None
            else:
                head = head.next
            return head

        prev = head
        for i in range(size - (n)):
            prev = head
            head = head.next

        if head == prev:
            head = head.next
            prev.next = None
            return head

        prev.next = head.next
        head.next = None
        head = start
        return head