'''
Difficulty: Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''
from collections import defaultdict
from typing import List

#Method-1: Brute force
#sort all strs in list. and hashmap sorted srts with actual strs

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for s in strs:
            sorted_strs.append(''.join(sorted(s)))
        
        grouped_strs = defaultdict(list)
        for i in range(len(strs)):
            grouped_strs[sorted_strs[i]].append(strs[i])
        
        return list(grouped_strs.values())
    
#Time: O(n*l*log(l)) l:avg length of each string
#Space: O(n)

#----------------------------------------------------------------------

#Method-2: without sorting strings
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            chars = [0] * 26 # a...z
            for c in s:
                chars[ord(c) - ord('a')] += 1
            ans[tuple(chars)].append(s)
        return ans.values()
    
#Time: O(n*l*26)
#Space: O(n)