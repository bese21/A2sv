# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        node = t = ListNode()
        l = []
        while temp is not None:
            l.append(temp.val)
            temp = temp.next
        
        d = Counter(l)
        for key, value in d.items():
            if value == 1:
                node.next = ListNode(key)
                node = node.next
        return t.next
