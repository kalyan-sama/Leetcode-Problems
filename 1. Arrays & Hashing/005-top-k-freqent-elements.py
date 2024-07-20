'''
Difficulty: Medium

Given an integer array nums and an integer k, return the k most frequent elements. 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
'''


from collections import Counter
from typing import List

#Method-1: hashmap + sort by values

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashmap = Counter(nums)
        sorted_by_value = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse = True))
        for key in sorted_by_value:
            ans.append(key)
            if len(ans) == k:
                return ans
            
#Time: O(nlogn)
#Space: O(n)

#----------------------------------------------------------------------

#Method-2: using Bucket sort
#create a bucket array with frequencies of values indexes and list of values as bucket value 
#Iterate from end of buckets(max repeated count) and add to ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashmap = Counter(nums)
        buckets = [[] for x in range(len(nums) + 1)] 
        for val, count in hashmap.items():
            buckets[count].append(val)
        
        for i in range(len(buckets) - 1, -1, -1):
            for x in buckets[i]:
                ans.append(x)
                if len(ans) == k:
                    return ans
                
#Time: O(n)
#Space: O(n)