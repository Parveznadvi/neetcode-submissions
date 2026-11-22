# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        
        counter=1
        curr=head
        leftNode=head
        while counter<left:
            leftNode=curr
            curr=curr.next
            counter+=1
        rightNode=curr
        fast=curr
        while counter<=right:
            fast=fast.next
            rightNode=fast
            counter+=1

        prev=rightNode
        curr=curr
        future=curr.next

        counter=0
        while counter<=(right-left):
            counter+=1
            curr.next=prev
            prev=curr
            curr=future
            if future!=None:
                future=future.next

        if leftNode==head and left!=2:
            return prev
        else:
            leftNode.next=prev
            return head