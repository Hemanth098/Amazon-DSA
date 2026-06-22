# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if head== None:
            return False
        fast = head.next
        
        while fast!= None:
            if slow == fast:
                print(slow.val,fast.val)
                return True
            if fast.next ==None:
                return False
            fast = fast.next.next
            slow = slow.next
        return False