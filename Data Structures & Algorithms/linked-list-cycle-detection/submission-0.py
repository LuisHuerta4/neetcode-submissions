# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = {}

        while node:
            if visited.get(node.val, 0) > 1:
                return True
            else:
                visited[node.val] = visited.get(node.val, 0) + 1
            node = node.next
        return False