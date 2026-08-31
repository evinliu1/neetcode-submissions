# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        GP = dummy

        while True:
            kth = self.findkth(GP, k)
            if not kth:
                break
            GN = kth.next

            prev, curr = kth.next, GP.next
            while curr != GN:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = GP.next
            GP.next = kth
            GP = tmp

        return dummy.next


    def findkth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node