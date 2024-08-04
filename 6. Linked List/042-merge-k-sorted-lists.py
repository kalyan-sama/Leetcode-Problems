'''
Difficulty: Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
'''

#Method-1: store all list nodes in an array anmd sort it

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next

        nums.sort()

        if not nums:
            return None
        dummy = ListNode()
        tail = dummy
        for n in nums:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy.next
    
#Time: O(k) + O(nlogn) + O(n) = O(nlogn) 
#Space: O(n)

#--------------------------------------------------------------------------------

#Method-2: Use merge 2 lists method. Divide and conquer
'''
The problem can be simplified by merging 2 lists at once. Repeat this method unntil all lists are merged
At first iteration, k lists are merged into k/2 lists i.e., 2 lists at a time
In next iteration, k/2 lists are merged into k/4 and so on until there is only one list left

The last list left is the final merged list
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = [] #Store k/n merged lists in a list

            for i in range(0, len(lists), 2): #Merge 2 lists at a time 
                l1 = lists[i]
                #If len of lists is even, then l1, l2 bot exists to merge
                #Otherwise, l2 will be None
                if (i + 1) < len(lists):
                    l2 = lists[i + 1] 
                else:
                    l2 = None 
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists #replace original list with mergedLists and contuinue iteration
        
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2: 
            tail.next = l2

        return dummy.next

#Time: O(klogn)
#Spce: O(k)
