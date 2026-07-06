class Solution:
    def rev(self, head: Optional[ListNode], prev_chain_end: Optional[ListNode], k: int):
        prev_node = None
        cur_node = head
        rev_chain_end = head

        for _ in range(k):
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        rev_chain_start = prev_node       
        next_chain_start = cur_node

        if prev_chain_end is not None:
            prev_chain_end.next = rev_chain_start

        return rev_chain_start, rev_chain_end, next_chain_start

    def get_sz(self, node: Optional[ListNode]) -> int:
        sz = 0
        while node is not None:
            sz += 1
            node = node.next
        return sz

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        final_head = None
        sz = self.get_sz(head)
        
        head_as_p = head
        prev_chain_end_as_p = None

        for i in range(sz // k):
            rev_chain_start, rev_chain_end, next_chain_start = self.rev(head_as_p, prev_chain_end_as_p, k)
            
            if final_head is None:
                final_head = rev_chain_start
            
            prev_chain_end_as_p = rev_chain_end
            head_as_p = next_chain_start

            if i == sz // k - 1 and sz % k != 0:
                rev_chain_end.next = next_chain_start

        return final_head