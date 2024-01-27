33. Search in Rotated Sorted Array
Medium
Topics
Companies
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
# 1st attempt
# finds pivot element in O(logn) time and then do search for target in O(logn) time.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left:int, right:int) -> int:
            # case when exactly one element if there
            if left==right:
                if nums[left]==target:
                    return left
                return -1

            target_index = -1
            while(left < right):
                mid = left + int((right-left)/2)
                if mid == left:
                    # handle case when left and right are adjacent
                    if target == nums[left]:
                        return left
                    if target == nums[right]:
                        return right
                    return -1
                m_value = nums[mid]
                if m_value == target:
                    return mid
                elif m_value > target:
                    right = mid
                elif m_value < target:
                    left = mid

        length = len(nums)
        # handle case when exactly one element is present
        if length == 1:
            if nums[0] == target:
                return 0
            return -1


        # search for the pivot point
        left = 0
        right = length - 1
        pivot_index = -1
        while(left < right):
            mid = left + int((right-left)/2)
            if mid == left:
                # handle case when left and right are adjacent
                pivot_index = right if nums[left] < nums[right] else left
                break
            l_value = nums[left]
            r_value = nums[right]
            m_value = nums[mid]
            if m_value > l_value:
                left = mid
            elif m_value < r_value:
                right = mid

        if pivot_index == length-1:
            target_index = binary_search(left=0, right=length-1)
        else:
            target_index = max(binary_search(left=0, right=pivot_index), binary_search(left=pivot_index+1, right=length-1))

        return target_index

# 2nd attempt (uses only one binary search)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        left = 0
        right = length-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
                































