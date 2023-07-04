# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        iterateKey = 1
        temp = head
        mapList = {}
        while temp:
            mapList[iterateKey] = ListNode(temp.val)
            temp = temp.next
            iterateKey+=1

        
        while left <= right:
            tempNode = mapList[left]
            mapList[left] = mapList[right]
            mapList[right] = tempNode
            left += 1
            right -= 1
        
        for i in range(1, len(mapList) + 1):
            if i != len(mapList):
                mapList[i].next = mapList[i+1]

        # print(len(mapList))
        return mapList[1]
