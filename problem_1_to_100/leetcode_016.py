"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        import numpy as np
        bias_lower = -np.inf
        bias_upper = np.inf
        for index in range(len(nums)-2):
            first = nums[index]
            left = index+1
            right = len(nums)-1
            while(left < right):
                second = nums[left]
                third = nums[right]
                three_sum = first + second + third
                bias = three_sum - target
                if bias == 0:
                    return target
                elif (bias < 0):
                    left += 1
                    if bias > bias_lower:
                        bias_lower = bias
                else:
                    right -= 1
                    if bias < bias_upper:
                        bias_upper = bias

        if bias_upper < -1*bias_lower:
            three_sum_closest = target + bias_upper
        else:
            three_sum_closest = target + bias_lower
        return three_sum_closest
"""
Same pattern as 3sum problem.
Learning:
    1. define clearly what variables you will be using for tracking 'close' number to given target.
    2. be very careful while deciding when to increment/decrement left or right pointer.
"""
