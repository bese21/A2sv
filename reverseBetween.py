# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        z=None
        i=0
        c=a=b=ListNode()
        xx=0
        while head:
            i=i+1
            if i>=left and i<right:
                x=head.next
                head.next=z
                z=head
                head=x
            elif i>right:
                break
            else:
                xx=1
                b.next=head
                b=b.next
                head=head.next
        if xx==0:
            return z
        b.next=z
        while a and a.next:
            a=a.next
        a.next=head
        return c.next
