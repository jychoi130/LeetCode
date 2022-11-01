# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ansList = []
        
        if(head == None): return None
        value = head.val
        
        ansList.append(value)
        next_node = head.next
        
        if next_node == None: return head
        
        while(next_node != None):
            ansList.append(next_node.val)
            next_node = next_node.next
        
        ans_head = ListNode(ansList[1])
        current = ans_head
        new_node = ListNode(ansList[0])
        current.next = new_node
        current = current.next
        
        for i in range(2, len(ansList)):
            if(i % 2 == 0):
                if(i+1 < len(ansList)):
                    new_node = ListNode(ansList[i+1])
                    current.next = new_node
                    current = current.next
                    new_node = ListNode(ansList[i])
                    current.next = new_node
                    current = current.next
                else: 
                    new_node = ListNode(ansList[i])
                    current.next = new_node
                    current = current.next
        
        return ans_head
        