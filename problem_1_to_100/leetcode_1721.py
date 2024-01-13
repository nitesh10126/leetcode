"""
1721. Swapping Nodes in a Linked List
Medium
Topics
Companies
Hint
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = ListNode(next=head)
        # s ........ None
        lF, F, rF = None, None, None
        lS, S, rS = None, None, None
        slow = start
        fast = start
        while(fast.next != None):
            if k > 0:
                lF = fast
                fast = fast.next
                k -= 1
                continue
            fast = fast.next
            slow = slow.next
        else:
            lS = slow

        F, rF = lF.next, lF.next.next
        S, rS = lS.next, lS.next.next

        if S == F:
            return start.next
        if F.next == S:
            lF.next = S
            lF.next.next = F
            lF.next.next.next = rS
        elif S.next == F:
            lS.next = F
            lS.next.next = S
            lS.next.next.next = rF
        else:
            lF.next = S
            lF.next.next = rF
            lS.next = F
            lS.next.next = rS
        
        return start.next





"""
In linked list traversal/pointer manipulation problem
 1. first take sufficient pointers to required node
 2. and manipulate them after.
 3. Don't try to use minimal pointer because it makes the problem difficult on cost of gaining nothing on space.

"""






















