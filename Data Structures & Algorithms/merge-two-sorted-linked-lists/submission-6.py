# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = []
        curr = list1
        curr1= list2
        while curr:
            out.append(curr.val)
            curr = curr.next
        while curr1:
            out.append(curr1.val)
            curr1=curr1.next
        merged = sorted(out)
        dummy = ListNode(0)
        curr = dummy
        for v in merged:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next
        
        