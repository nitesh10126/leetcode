'''
	Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

	Example 1:

	Input: "babad"
	Output: "bab"
	Note: "aba" is also a valid answer.
	Example 2:

	Input: "cbbd"
	Output: "bb"
'''

class Solution(object):
	def longestPallindrome(self, s):
		s_len = len(s)
		isPallin = [[0 for _ in range(s_len)] for _ in range(s_len)]
		for i in range(s_len):
			isPallin[i][i] = True

		pallin_start, pallin_end = 0, 0
		
		substring_size = 2
		while substring_size <= s_len:
			for start in range(s_len):
				end = start + substring_size - 1
				if end >= s_len:
					continue

				if s[start] == s[end]:
					isPallin[start][end] = isPallin[start+1][end-1] if substring_size > 2 else True
				else:
					isPallin[start][end] = False

			if isPallin[start][end]:
				pallin_start = start
				pallin_end = end
			
			substring_size += 1
		return s[pallin_start:pallin_end+1]

# Learning: 
# 1. make sure indices of dp does not go outOfIndex
# 2. for substring_size == 2, `isPallin[start+1][end-1]` goes out of bound. (failed to get it in first attempt)

