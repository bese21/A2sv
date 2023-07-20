# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_left = tail_left = ListNode(0)
        head_right = tail_right = ListNode(0)
        while head:
            if head.val < x:
                tail_left.next = head
                tail_left = tail_left.next
            else:
                tail_right.next = head
                tail_right = tail_right.next
            head = head.next
        tail_right.next = None
        tail_left.next = head_right.next
        return head_left.next
