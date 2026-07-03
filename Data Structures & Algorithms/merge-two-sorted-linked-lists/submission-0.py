# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def move_next(node: Optional[ListNode]):
        if node is None:
            return None
        return node.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node1 = list1
        cur_node2 = list2

        prev_node = None
        cur_node = None
        head = None
        inf = int(2e9)
        while cur_node1 is not None or cur_node2 is not None:
            first_node_val = (inf if cur_node1 is None else cur_node1.val)
            second_node_val = (inf if cur_node2 is None else cur_node2.val)

            prev_node = cur_node
            cur_node = ListNode(val=min(first_node_val, second_node_val))
            if prev_node is not None:
                prev_node.next = cur_node
            if head is None:
                head = cur_node
                
            if first_node_val < second_node_val:
                cur_node1 = cur_node1 if cur_node1 is None else cur_node1.next
            else:
                cur_node2 = cur_node2 if cur_node2 is None else cur_node2.next
        return head
                