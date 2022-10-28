# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        allist = []
        answer = ListNode()
        
        if(list1 == None):                        
            if(list2 != None):                        
                node2 = list2.next
                allist.append(list2.val)
            else:
                return list1
        else: 
            node1 = list1.next
            allist.append(list1.val)
            if(list2 != None):
                node2 = list2.next
                allist.append(list2.val)
        
        if(list1 != None):
            while(node1 != None):
                allist.append(node1.val)
                node1 = node1.next
        if(list2 != None):
            while(node2 != None):
                allist.append(node2.val)
                node2 = node2.next
            
        allist.sort()
        
        check = []
        for node in allist:
            nodelist = ListNode(node)
            check.append(nodelist)
        
        for i in range(0,len(check)-1):
            check[i].next = check[i+1]
        check[len(check)-1].next = None
        
        return(check[0])
            