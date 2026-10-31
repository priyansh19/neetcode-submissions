# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        new_head = stack.pop()
        prev = new_head
        while stack:
            prev.next = stack.pop()
            prev = prev.next
        prev.next = None
        return new_head