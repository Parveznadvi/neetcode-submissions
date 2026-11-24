# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None:
            return True
        if head.next.next==None:
            if head.val==head.next.val:
                return True
            else:
                return False

        listLen=1
        curr=head
        while curr!=None:
            curr=curr.next
            listLen+=1

        # Find middle of the LinkedList:
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        if listLen//2==0:
            head2=slow
        else:
            head2=slow.next

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

        #Compare both the lists:
        p1=head
        p2=head3
        while p2!=None:
            if p1.val!=p2.val:
                return False
            p1=p1.next
            p2=p2.next
        
        return True
