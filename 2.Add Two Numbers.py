# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        def toList(ln):# convert listnode to list
            a=[]
            while ln.next!=None:
                a.append(ln.val)
                ln=ln.next
            a.append(ln.val)
            return a
        a,b=toList(l1),toList(l2)
        n,m=len(a),len(b)
        i,j=0,0
        c=[]
        x=0
        while i<n and j<m:
            c.append((a[i]+b[j]+x)%10)
            x=(a[i]+b[j]+x)//10
            i+=1
            j+=1
        while i<n:
            c.append((a[i]+x)%10)
            x=(a[i]+x)//10
            i+=1
        while j<m:
            c.append((b[j]+x)%10)
            x=(b[j]+x)//10
            j+=1
        if x>0:
            c.append(x)
        print(c)    
        l3=ListNode(c[-1])    
        for i in range(len(c)-2,-1,-1):
            lst=ListNode(c[i])
            lst.next=l3
            l3=lst
        return l3    
