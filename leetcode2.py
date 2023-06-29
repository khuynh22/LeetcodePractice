# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        store = 0
        curr1 = l1
        curr2 = l2
        res = ListNode()
        currRes = res
        while curr1 != None and curr2 != None:
            if curr1.val + curr2.val + store < 10:
                currRes.val = curr1.val + curr2.val + store
                store = 0
            else:
                currRes.val = curr1.val + curr2.val + store - 10
                store = 1
            if curr1.next == None or curr2.next == None:
                currRes.next = None
            else:
                currRes.next = ListNode()
                currRes = currRes.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1 != None:
            currRes.next = ListNode()
            currRes = currRes.next
            if curr1.val + store < 10:
                currRes.val = curr1.val + store
                store = 0
            else:
                currRes.val = curr1.val + store - 10
                store = 1
            curr1 = curr1.next
            
        while curr2 != None:
            currRes.next = ListNode()
            currRes = currRes.next
            if curr2.val + store < 10:
                currRes.val = curr2.val + store
                store = 0
            else:
                currRes.val = curr2.val + store - 10
                store = 1
            curr2 = curr2.next
        if store == 1:
            currRes.next = ListNode()
            currRes = currRes.next
            currRes.val = 1
        return res