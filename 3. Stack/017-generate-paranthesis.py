'''
Difficulty: Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
 
'''

#Method-1: using stack

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #C-1: Add '(' only if  curr_open > n
        #C-2: Add ')' only if curr_close < curr_open
        #C-3: if curr_open == curr_close == n, then valid paranthesis formed

        stack = []
        ans = []

        def backtrack(curr_open, curr_close):
            if curr_open == curr_close == n:
                ans.append(''.join(stack))
                return
            
            if curr_open < n:
                stack.append('(')
                backtrack(curr_open + 1, curr_close)
                stack.pop()
            
            if curr_close< curr_open:
                stack.append(')')
                backtrack(curr_open, curr_close + 1)
                stack.pop()
        
        backtrack(0, 0)
        return ans
        

#Method-2: without using stack

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #C-1: Add '(' only if  curr_open > n
        #C-2: Add ')' only if curr_close < curr_open
        #C-3: if curr_open == curr_close == n, then valid paranthesis formed

        ans = []

        def backtrack(curr_open, curr_close, s):
            if curr_open == curr_close == n:
                ans.append(s)
                return
            
            if curr_open < n:
                backtrack(curr_open + 1, curr_close, s+'(')
            
            if curr_close< curr_open:
                backtrack(curr_open, curr_close + 1, s+')')
        
        backtrack(0, 0, '')
        return ans
        