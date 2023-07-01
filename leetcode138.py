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
        if head == None:
            return None
        
        mapNode = {}
        curr = head
        while curr:
            mapNode[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head

        while curr:
            if curr.next:
                mapNode[curr].next = mapNode[curr.next]

            if curr.random:
                mapNode[curr].random = mapNode[curr.random]
            
            curr = curr.next
        return mapNode[head]