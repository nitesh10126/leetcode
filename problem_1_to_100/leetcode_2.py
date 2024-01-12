# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        isFirst = True
        carry = 0
        while((l1 is not None) & (l2 is not None)):
            value = (l1.val + l2.val + carry)%10
            carry = 1 if (l1.val + l2.val + carry) > 9 else 0
            
            if isFirst:
                node = ListNode(value)
                firstNode = node
                isFirst = False
            else:
                new = ListNode(value)
                node.next = new
                node = new

            l1 = l1.next
            l2 = l2.next

        while(l1 is not None):
            value = (l1.val + carry) % 10
            carry = 1 if (l1.val + carry) > 9 else 0
            new = ListNode(value)
            node.next = new
            node = new
            l1 = l1.next

        while(l2 is not None):
            value = (l2.val + carry) % 10
            carry = 1 if (l2.val + carry)>9 else 0
            new = ListNode(value)
            node.next = new
            node = new
            l2 = l2.next

        if carry > 0:
            new = ListNode(carry)
            node.next = new
            node = new

        return firstNode
