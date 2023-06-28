# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        walker = head
        runner = head
        while runner.next and runner.next.next:
            runner = runner.next.next
            walker = walker.next
            if runner == walker:
                return True

        return False
