# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        aSize=0
        bSize=0
        aHead=headA
        bHead=headB
        while aHead!=None:
            aHead=aHead.next
            aSize+=1
        while bHead!=None:
            bHead=bHead.next
            bSize+=1

        if aHead!=bHead:
            return None

        aHead=headA        
        while(aSize>bSize):
            aHead=aHead.next
            aSize-=1
        bHead=headB
        while(bSize>aSize):
            bHead=bHead.next
            bSize-=1

        while(aHead!=bHead):
            aHead=aHead.next
            bHead=bHead.next
        
        return aHead

    


        