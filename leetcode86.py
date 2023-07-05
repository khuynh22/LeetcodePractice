# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = []
        large = []
        temp = head
        if not head or not head.next:
            return head
        while temp:
            if temp.val >= x:
                large.append(ListNode(temp.val))
            else:
                small.append(ListNode(temp.val))
            temp = temp.next
        
        for i in range(len(small) - 1):
            small[i].next = small[i+1]

        if small and large:
            small[-1].next = large[0]
        
            for i in range(len(large) - 1):
                large[i].next = large[i+1]

            return small[0]
        elif not large:
            return small[0]
        else:
            for i in range(len(large) - 1):
                large[i].next = large[i+1]

            return large[0]