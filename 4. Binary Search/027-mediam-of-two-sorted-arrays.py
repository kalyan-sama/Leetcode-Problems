'''
Difficulty:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        i, j = 0, 0
        ans = 0
        while i <= len(nums1) - 1 and j <= len(nums2) - 1:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i <= len(nums1) - 1:
            merged.append(nums1[i])
            i += 1
         
        while j <= len(nums2) - 1:
            merged.append(nums2[j])
            j += 1


        if len(merged)%2 == 0:
            mid = len(merged)//2
            print(mid)
            ans = (float(merged[mid]) + merged[mid-1])/2
        else:
            mid = len(merged)//2 
            ans = merged[mid]

        return (ans)
            
#Time: O(M + N)
#Space: O(M + N)