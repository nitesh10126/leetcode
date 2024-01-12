"""
18. Remove Nth Node from End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two Pass Solution: O(n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        start = head
        while(start.next is not None):
            length += 1
            start = start.next
        n_from_start = length - n + 1
        if n_from_start == 1:
            head = head.next
            return head

        start = head
        for i in range(n_from_start-1):
            previous = start
            start = start.next
        previous.next = start.next
        return head

# One Pass Solution using two-pointer moving window approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Use two-pointer moving window approach"""
        fast = ListNode(next=head)
        slow = ListNode(next=head)

        for i in range(n):
            fast = fast.next

        if fast.next == None: return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head        

"""
Key Learning:
1. Two pointer moving window method
2. Edge case when it's first node to be removed, return the pointer carefully.
"""
