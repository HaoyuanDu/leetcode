# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        car = 0
        root = result = ListNode(0)
        while l1 or l2 or car: 
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            
            car, cur = divmod(val1 + val2 + car, 10)
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
           # result.next = result = ListNode(cur)
            result.next = ListNode(cur)
            result = result.next

        return root.next
       