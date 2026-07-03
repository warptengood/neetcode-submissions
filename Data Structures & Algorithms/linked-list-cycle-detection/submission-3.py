# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        start = True

        while True:
            if not start and fast == slow:
                return True
            start = False
            if fast is not None and fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
            else:
                return False
            
            slow = slow.next
