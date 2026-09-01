# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gpre = dummy

        while True:
            kth = self.findkth(gpre, k)
            if not kth:
                break
            gnext = kth.next

            prev, curr = kth.next, gpre.next

            while curr != gnext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # self.testhead(dummy)
            temp = gpre.next
            gpre.next = kth
            temp.next = gnext
            gpre = temp
        
        return dummy.next



        
    def findkth(self, node, k):
        while node and k > 0:
            node = node.next
            k -=1
        return node

    def testhead(self, node):
        while node:
            print(node.val)
            node = node.next
