# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def out(l: Optional[ListNode]):
            if l is None:
                return
            print(l.val, end=', ')
            out(l.next)

        def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            if l1 is None and l2 is None:
                return None
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            
            head = None
            prev_node = None

            while l1 is not None or l2 is not None:
                l1_val = int(2e9) if l1 is None else l1.val
                l2_val = int(2e9) if l2 is None else l2.val
                new_node = ListNode(min(l1_val, l2_val))
                if l1_val < l2_val:
                    l1 = l1 if l1 is None else l1.next
                else:
                    l2 = l2 if l2 is None else l2.next
                if prev_node is None:
                    head = new_node
                else:
                    prev_node.next = new_node
                prev_node = new_node
            return head
        
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = merge(lists[i], lists[i - 1])
        return lists[-1]

