# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        prev_node = None

        while True:
            smallest_node = None
            smallest_node_idx = -1

            for i, ll in enumerate(lists):
                if ll is not None:
                    if smallest_node is None:
                        smallest_node = ll
                        smallest_node_idx = i
                    else:
                        if smallest_node.val > ll.val:
                            smallest_node = ll
                            smallest_node_idx = i

            if smallest_node == None:
                break
            
            new_node = ListNode(smallest_node.val)
            if prev_node is not None:
                prev_node.next = new_node
            else:
                head = new_node
            prev_node = new_node

            lists[smallest_node_idx] = lists[smallest_node_idx].next

        return head