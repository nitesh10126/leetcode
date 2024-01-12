class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize two pointers
        left = 0
        right = len(height) - 1
        
        if len(height) == 2:
            return min(height[0], height[1])

        max_area = 0
        while(left < right):
            min_index = left if height[left] <= height[right] else right
            max_area = max(max_area, height[min_index] * (right - left))
            if min_index == left:
                left += 1
            else:
                right -= 1
        return max_area

"""
If it is hard to get effecient approach than O(n2) complexity. Try Dynamic Programming first, if it fails Try Two-Pointer approach.
It should give O(n) solution. Mostly becuase problems underlying structure. 
"""
