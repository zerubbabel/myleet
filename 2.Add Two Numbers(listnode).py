# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# operate on ListNode
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3=ListNode(0)
        last=l3
        c=0
        while l1!=None and l2!=None:   
            s=l1.val+l2.val+c
            t=ListNode(s%10)
            c=s // 10
            last.next=t
            last=t
            l1=l1.next
            l2=l2.next
        while l1!=None:
            s=l1.val+c
            t=ListNode(s%10)
            c=s // 10
            last.next=t
            last=t
            l1=l1.next
        while l2!=None:
            s=l2.val+c
            t=ListNode(s%10)
            c=s // 10
            last.next=t
            last=t
            l2=l2.next
        if c>0:
            t=ListNode(c)
            last.next=t
        return l3.next    
            
            