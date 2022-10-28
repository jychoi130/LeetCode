# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head
        
        value = []
        value.append(head.val)
        nex = head.next
        
        while(nex!=None):
            value.append(nex.val)
            nex = nex.next
            
        value.reverse()
        
        ans = []
        for i in range(0, len(value)):
            tempNode = ListNode(value[i])
            ans.append(tempNode)
        
        for i in range(0, len(ans)-1):
            ans[i].next = ans[i+1]
            
        ans[len(ans)-1].next = None
        
        return ans[0]