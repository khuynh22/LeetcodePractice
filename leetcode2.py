# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        resRet = res
        plusOne = 0
        p1 = l1
        p2 = l2
        while p1 and p2:
            res.val = p1.val + p2.val + plusOne
            if res.val >= 10:
                res.val -= 10
                plusOne = 1
            else:
                plusOne = 0

            if p1.next == None and p2.next == None:
                res.next = None
            else:
                res.next = ListNode()
                res = res.next

            p1 = p1.next
            p2 = p2.next

        while p1:
            res.val = p1.val + plusOne
            
            if res.val >= 10:
                res.val -= 10
                plusOne = 1
            else:
                plusOne = 0

            if p1.next == None:
                res.next = None
            else:
                res.next = ListNode()
                res = res.next
            p1 = p1.next

        

        while p2:
            res.val = p2.val + plusOne
            
            if res.val >= 10:
                res.val -= 10
                plusOne = 1
            else:
                plusOne = 0

            if p2.next == None:
                res.next = None
            else:
                res.next = ListNode()
                res = res.next
            p2 = p2.next

        if plusOne == 1:
            res.next = ListNode(1)
        return resRet