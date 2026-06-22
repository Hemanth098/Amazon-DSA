# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        x= head.next
        if x.next == None:
            x.next = head
            head.next = None
            return x
        y = x.next
        head.next = None
        while y.next != None:
            x.next = head
            head = x
            x = y
            y = y.next
        x.next = head
        y.next = x
        return y
