# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        Node = []
        
        if (head == None):
            return head
        
        nextNode = head.next
        if(nextNode == None): return head
        
        Node.append(head.val)
        
        while(nextNode != None):
            Node.append(nextNode.val)
            nextNode = nextNode.next
        
        sub = Node[left-1: right]
        sub = list(reversed(sub))
        
        Node[left-1 : right] = sub
        
        ans = ListNode(Node[0])
        current = ans
        
        for i in range(1,len(Node)):
            new_node = ListNode(Node[i])
            current.next = new_node
            current = current.next
        
        return ans