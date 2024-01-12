"""
22. Generate Parantheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
# iterative method
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_list = ["()"]
        if n==1:
            return valid_list

        while n > 1:
            n -= 1
            new_valid_set = set()
            for parantheses in valid_list:
                parity = 0
                new_valid_set.add("()"+parantheses)
                for i, bracket in enumerate(parantheses):
                    if bracket == "(":
                        parity += 1
                    else:
                        parity -= 1

                    if i == len(parantheses)-1:
                        new_valid_set.add("(" + parantheses + ")")
                        continue

                    if parity == 0:
                        new_paran = "(" + parantheses[0:i+1] + ")" + parantheses[i+1:]
                        new_valid_set.add(new_paran)

            valid_list = list(new_valid_set)
        return valid_list                    

# recursive method
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        list_of_valid_parenthesis = list()

        def backtrack(S, left, right):
            if len(S) == 2*n:
                list_of_valid_parenthesis.append(S)
                return

            if left < n:
                backtrack(S+'(', left+1, right)

            if right < left:
                backtrack(S+')', left, right+1)

        backtrack('', 0, 0)
        return list_of_valid_parenthesis

"""
Number of valid parentesis of length 2n is Catalan number = (2n)!/(n!)((n+1)!)
https://en.wikipedia.org/wiki/Catalan_number
"""
