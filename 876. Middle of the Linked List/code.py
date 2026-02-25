class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        empty = []
        
        iteration = head
        while iteration:
            empty.append(iteration.val)
            iteration = iteration.next
        
        value = empty[-3:]
        return value
