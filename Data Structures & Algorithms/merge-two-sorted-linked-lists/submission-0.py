# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        elif list2 is None: return list1

        if list1.val > list2.val:
            head_new = list2
        else:
            head_new = list1

        res_head = head_new
        head_i, head_j = list1, list2
        while list1 or list2:
            if list1.val > list2.val:
                head_new.next = list2
                list2 = list2.next
            else:
                head_new.next = list1
                list1 = list1.next
        return res_head