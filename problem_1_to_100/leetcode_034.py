"""
34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 0:
            return [-1, -1]

        if length == 1:
            return [0, 0] if target == nums[0] else [-1, -1]

        left = 0
        right = length - 1
        while left < right:
            mid = left + ((right-left)//2)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] < target or nums[left] > target:
            return [-1, -1]

        first_occurance = left

        left = 0
        right = length - 1
        while left < right:
            mid = left + ((right-left+1)//2)
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        last_occurance = left
        return [first_occurance, last_occurance]
"""
clever use of two binary-search.
Nice read: https://www.topcoder.com/thrive/articles/Binary+Search
"""
