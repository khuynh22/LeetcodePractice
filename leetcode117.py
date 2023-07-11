"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = []
        node = root
        queue.append(node)

        while len(queue) > 0:
            for i in range(len(queue) - 1):
                queue[i].next = queue[i + 1]

            queue[-1].next = None
            n = len(queue)
            for i in range(n):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)

                queue.pop(0)

        return root
