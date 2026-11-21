# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head==None:
            return False
        
        slow=head
        fast=head

        while fast!=None:            
            if fast.next==None or fast.next.next==None:
                return False
            else:
                slow=slow.next
                fast=fast.next.next
            if fast==slow:
                return True
        
        return False

