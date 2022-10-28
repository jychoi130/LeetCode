# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        revValues = []
        
        if  head.val != None:
            values.append(head.val)
        else : return True
        
        try:
            check = head.next
        except: return True
        
        checkstr = "head.next"
        
        while(check != None):
            values.append(check.val)
            check = check.next
            
        for item in values[::-1]:
            revValues.append(item)
        
        if values == revValues:
            return True
        else: return False