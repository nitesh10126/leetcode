"""
24. Swap Nodes in Pairs
Medium
Topics
Companies
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My First Solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next == None):
            return head

        first = head
        second = first.next
        third = second.next
        head = second
        while(third != None):
            prev = first
            second.next = first
            first.next = third
            if (third == None) or (third.next == None):
                break
            first = third
            second = first.next
            third = second.next
            prev.next = second
        else:
            second.next = first
            first.next = third

        return head

# better implementation
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode(0)
        s.next = head
        l = s
        while l.next and l.next.next :
            rr = l.next.next
            l.next.next = l.next.next.next
            rr.next = l.next
            l.next = rr
            l = l.next.next
        return s.next     



























