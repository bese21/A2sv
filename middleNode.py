# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0 
        
        # find length of linkedlist
        temp = head
        while temp is not None:
            length = length + 1
            temp = temp.next

        mid_idx = ceil(length/2)

        if length % 2 == 0 :
            mid_idx = mid_idx + 1
        
        mid_node = head
        for i in range(mid_idx-1):
            mid_node = mid_node.next

        return mid_node
