# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = ListNode()
        res = cur_node
        carry = 0
        while l1 is not None or l2 is not None:
            cur_val = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val)
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            cur_val += carry
            carry = cur_val // 10
            cur_val %= 10
            cur_node.val = cur_val

            if l1 is not None or l2 is not None:
                cur_node.next = ListNode()
                cur_node = cur_node.next

        if carry != 0:
            cur_node.next = ListNode(carry)
        return res
                