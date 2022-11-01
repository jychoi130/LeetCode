# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1Next = l1.next
        list1Value = str(l1.val)
        list2Next = l2.next
        list2Value = str(l2.val)
        
        while(list1Next != None):
            list1Value += str(list1Next.val)
            list1Next = list1Next.next
        
        while(list2Next != None):
            list2Value += str(list2Next.val)
            list2Next = list2Next.next
            
        list1Value = "".join(reversed(list1Value))
        list2Value = "".join(reversed(list2Value))
        
        a = int(list1Value) + int(list2Value)
        StrAns = str(a)
        StrAns = "".join(reversed(StrAns))
        
        head = ListNode(int(StrAns[0]))
        current = head
        
        for i in range(1, len(StrAns)):
            new_node = ListNode(int(StrAns[i]))
            current.next = new_node
            current = current.next
            
        return head