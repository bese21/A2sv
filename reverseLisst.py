class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head:
            ans.append(head)
            head = head.next

        ansHead = None
        prev = None
        first = True

        for i in reversed(ans):
            if first:
                ansHead = i
                prev = i
                first = False
                continue
            i.next = None
            prev.next = i
            prev = i
            
        return ansHead
            
