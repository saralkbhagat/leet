# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        cur=head
        
        i=0
        while(cur!=None):
            cur=cur.next
            i=i+1   
            
        cur=head
        def reverse(cur):
            lenn=i 
            localhead=cur
            prev=None
            
            length=0
            count=0
            if cur is None :
                return 
            

            j=0
            if lenn>=k:
                while(cur!=None and j<k):
                    lenn=lenn-1
                    j=j+1

                    temp=cur.next
                    cur.next=prev
                    prev=cur
                    cur=temp
                
                lastnode=prev
            else:lastnode=cur
            
                
            
            
            localhead.next=reverse(cur)
           

            return lastnode
        return reverse(head)



        
# @lc code=end


        