# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Node = []
        
        if(head==None):
            return head
        value = head.val
        Node.append(value)
        nextNode = head.next
        
        if(nextNode == None):
            return head
        
        while(nextNode):
            Node.append(nextNode.val)
            nextNode = nextNode.next
        
        popCount = 0
        for i in range(0, len(Node)):
            if(i%2==0):
                continue
            else:
                temp = Node.pop(i-popCount)
                popCount += 1
                Node.append(temp)
        
        ans = ListNode(Node[0])
        current = ans
        new_node = ListNode(Node[1])
        current.next = new_node
        current = current.next
        
        for i in range(2, len(Node)):
            new_node = ListNode(Node[i])
            current.next = new_node
            current = current.next
            
        return ans