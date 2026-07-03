# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_node = head
        
        sz = 0
        while cur_node is not None:
            sz += 1
            cur_node = cur_node.next
        n = sz - n + 1
        if n == 1:
            head = head.next
            return head
            
        cur_cnt = 0
        cur_node = head
        prev_node = None
        while cur_cnt < n:
            if cur_cnt + 1 == n - 1:
                prev_node = cur_node
            cur_cnt += 1
            cur_node = cur_node.next

        prev_node.next = prev_node.next.next
        return head