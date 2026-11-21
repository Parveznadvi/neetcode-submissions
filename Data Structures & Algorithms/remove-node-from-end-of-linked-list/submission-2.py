# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next==None:
            return None

        slow=head
        sz=0
        while slow!=None:
            slow=slow.next
            sz+=1

        rmNode = sz-n
        counter=1
        slow=head
        while counter<rmNode:
            slow=slow.next
            counter+=1

        if counter==1 and rmNode!=1:
            head=head.next

        slow.next=slow.next.next
        return head