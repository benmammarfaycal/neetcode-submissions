# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        current=slow.next
        slow.next=None
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        first=head
        second=prev
        while second:
            nxt1=first.next
            nxt2=second.next
            first.next=second
            second.next=nxt1
            first=nxt1
            second=nxt2

            
         