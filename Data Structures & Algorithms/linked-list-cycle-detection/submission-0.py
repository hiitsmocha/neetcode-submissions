# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        cycle = False
        cur = head
        index = 0
        while cycle != True and cur:
            if cur in hashmap:
                cycle = True
                return True
            hashmap[cur] = index
            index += 1
            cur = cur.next
        return False
        
