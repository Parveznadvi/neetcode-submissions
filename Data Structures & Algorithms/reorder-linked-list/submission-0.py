# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head.next==None or head.next.next==None:
            return
        
        # Find middle of the LinkedList:
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        head2=slow.next
        slow.next=None

        #Reverse Linkedlist at head2:
        prev=None
        curr=head2
        future=head2.next

        while(curr!=None):
            curr.next=prev
            prev=curr
            curr=future
            if future!=None:
                future=future.next        
        head3=prev

        #Merge both the lists:
        p1=head
        p2=head3
        while p2!=None:
            temp=p1.next
            p1.next=p2
            p2=p2.next
            p1.next.next=temp
            p1=temp









