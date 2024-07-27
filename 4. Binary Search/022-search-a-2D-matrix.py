'''
Difficulty: Medium

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example-1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example-2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        rowLeft, rowRight = 0, m - 1
        colLeft, colRight = 0, n - 1

        while rowLeft <= rowRight:
            rowMid = (rowLeft + rowRight) //2

            if matrix[rowMid][0] == target or matrix[rowMid][n -1] == target:
                return True
            
            elif matrix[rowMid][0] > target :
                rowRight = rowMid - 1

            elif matrix[rowMid][0] < target and matrix[rowMid][n -1] < target:
                rowLeft = rowMid + 1

            else:
                break
                
        while colLeft <= colRight:
            colMid = (colLeft + colRight) //2
            print(matrix[rowMid][colMid])
            if matrix[rowMid][colMid] == target:
                return True
                
            elif matrix[rowMid][colMid] > target:
                colRight = colMid - 1
            else:
                colLeft = colMid + 1

        return False

#Time: O(logm + logn)
#Space: O(1)