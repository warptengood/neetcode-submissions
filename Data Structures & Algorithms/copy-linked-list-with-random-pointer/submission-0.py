"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}
        cur_node = head
        new_head = None
        while cur_node is not None:
            new_node = Node(cur_node.val)
            map[cur_node] = new_node
            if new_head is None:
                new_head = new_node
            cur_node = cur_node.next
        cur_node = head
        while cur_node is not None:
            if cur_node.next in map:
                map[cur_node].next = map[cur_node.next]
            if cur_node.random in map:
                map[cur_node].random = map[cur_node.random]
            cur_node = cur_node.next
        return new_head