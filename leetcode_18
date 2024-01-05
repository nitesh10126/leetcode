"""
18. 4SUM
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
        nums.sort()
        quadruplets = set()
        for index1 in range(len(nums)-3):
            first = nums[index1]
            for index2 in range(index1+1, len(nums)-2):
                second = nums[index2]
                left = index2+1
                right = len(nums)-1
                while(left < right):
                    third = nums[left]
                    fourth = nums[right]
                    four_sum = first + second + third + fourth
                    if four_sum == target:
                        quadruplets.add((first, second, third, fourth))
                        left += 1
                        right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return list(quadruplets)
