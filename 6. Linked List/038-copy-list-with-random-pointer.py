'''
Difficulty: Medium

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

https://leetcode.com/problems/copy-list-with-random-pointer/description/
'''

#Method-1: Naive approach 
'''
Create a copy of the old list, but only with the next pointers.

Traverse through the copy list and check the corresponding random pointers in the old list. Map random pointers accordingly.
'''

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy = Node(0)
        tail = dummy

        curr = head

        #Copy the old list into the new list
        while curr:
            val = curr.val
            node = Node(val)
            tail.next = node
            curr = curr.next
            tail = tail.next
        
        #Traverse the old list and upadte the random pointer of each node in the copy list
        a, b = head, dummy.next
        while a:
            if a.random is None:
                b.random = None
            else:
                #For each node, we have to check the random pointer from the beginning to the end of the list.
                k1, k2 = head, dummy.next
                while a.random is not k1:
                    k1 = k1.next
                    k2 = k2.next
                b.random = k2
            a = a.next
            b = b.next
        
        return dummy.next

#Time: O(n^2)
#Space: O(n)

#----------------------------------------------------------------------------------------------------------------------

#Method-2: Use a hashmap to store the corresponding nodes of old and new lsits
'''
We can use a hashmap to map the old nodes to new nodes.
This way, we can directly get the random pointer of the node without having to traverse through the entire list
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToNew = { None: None } # When node is pointing to None, corresponding copy node should also point to None
        dummy = Node(0)
        tail = dummy

        curr = head
        while curr:
            val = curr.val
            node = Node(val)
            oldToNew[curr] = node #Map the new node to old node
            tail.next = node
            curr = curr.next
            tail = tail.next
        
        curr, new = head, dummy.next
        while curr:
            #If curr.random is pointing to X inold list, 
            # then new.random should point to the corresponding node of X in hashmap, which will be oldToNew[X]
            new.random = oldToNew[curr.random] 
            curr = curr.next
            new = new.next

        return dummy.next

#Time: O(n)
#Space: O(n)
