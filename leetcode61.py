# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next

        for i in range((k % count)):
            head = self.rotateOne(head)
        return head

    
    def rotateOne(self, head):
        prev, last = self.getLast(head)
        prev.next = None
        last.next = head
        return last

    def getLast(self, head):
        count = 0
        temp = head
        prev = temp
        while temp.next:
            count += 1
            prev = temp
            temp = temp.next
        return prev, temp