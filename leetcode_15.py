"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
	    if (len(nums) == 3) & (sum(nums) == 0):
            return [[nums[0], nums[1], nums[2]]]
        nums.sort()
        triplets = list()
        for index in range(len(nums)-2):
            first = nums[index]
            left = index+1
            right = len(nums)-1
            while left < right:
                second = nums[left]
                third = nums[right]
                three_sum = first + second + third
                if three_sum == 0:
                    triplets.append((first, second, third))
                    left += 1
                    right -= 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        triplets = set(triplets)
        triplets = [[i, j, k]for (i, j, k) in triplets]
        return triplets

"""
A good question asking to apply two-pointer approach effeciently. 
O(n2) solution.
"""
