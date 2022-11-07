# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None : return lists
        allList = []
        for i in lists:
            if i == None: continue
            allList.append(i.val)
            nextNode = i.next
            while(nextNode != None):
                allList.append(nextNode.val)
                nextNode = nextNode.next
        
        if len(allList) == 0: return None
        allList.sort()
        head = ListNode(allList[0])
        current = head
        for i in range(1, len(allList)):
            new_node = ListNode(allList[i])
            current.next = new_node
            current = current.next
        
        return head