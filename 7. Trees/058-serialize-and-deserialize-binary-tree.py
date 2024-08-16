'''
Diffuclty: Hard

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        self.preorder = ''

        def preorderTraversal(node):
            if not node:
                self.preorder += 'null,'
                return
            self.preorder += str(node.val) + ','
            preorderTraversal(node.left)
            preorderTraversal(node.right)
        print(self.preorder)
        preorderTraversal(root)
        return self.preorder.rstrip(',')


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == 'null':
            return None
        preorder = data.split(',')
        print(preorder)
        self.i = 0
        def constructor():
            if  preorder[self.i] == 'null':
                self.i += 1
                return None
            print('i = ', self.i)
            print(preorder[self.i])
            root = TreeNode(preorder[self.i])

            self.i += 1
            root.left = constructor()
            root.right = constructor()
            return root
        return constructor()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))