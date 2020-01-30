"""
100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_sametree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype : bool
        """
        if p == None and q == None:
            return True
        if (p != None and q == None) or (p == None and q != None) or (p.val != q.val):
            return False
        return self.is_sametree(p.left, q.left) and self.is_sametree(p.right, q.right)


    def string_to_treenode(self, inputs):
        input = inputs.strip()
        inputs = input[1:-1]
        if not input:
            return None

        toggle = 0
        nums = [s.strip() for s in inputs.split(',')]
        q = deque()
        root = TreeNode(int(nums[0]))
        q.append(root)

        i = 1
        cnt = len(nums)
        while i < cnt:
            node = q.popleft()

            for j in range(2):
                if nums[i] != "null":
                    new_node = TreeNode(int(nums[i]))
                    q.append(new_node)
                    if j == 0:
                        node.left = new_node
                    else: 
                        node.right = new_node
                i += 1
                if i >= cnt:
                    break
        return root        


    def list_to_treenode(self, nums):
        if not nums:
            return None

        root = TreeNode(nums[0])
        q = deque()
        q.append(root)
        toggle = 0

        i = 1
        cnt = len(nums)
        while i < cnt:
            node = q.popleft()

            for j in range(2):
                if nums[i] != None:
                    new_node = TreeNode(nums[i])
                    q.append(new_node)
                    if j == 0:
                        node.left = new_node
                    else: 
                        node.right = new_node
                i += 1
                if i >= cnt:
                    break
        return root

def test_int_nums():
    test_cases = [
        { "p": [1,2,3]       , "q": [1,2,3] },
        { "p": [1,2]         , "q": [1,None,2] },
        { "p": [1,2,1]       , "q": [1,1,2] },
        { "p": [1,2,5,6,9,10], "q": [1,2,5,6,9,10]}
    ]
    sol = Solution()
    print("\n ------ [Test Int Numbers] -----")
    for i, test_case in enumerate(test_cases, 1):
        p = sol.list_to_treenode(test_case["p"])
        q = sol.list_to_treenode(test_case["q"])
        res = sol.is_sametree(p, q)
        print(f"{i}. {test_case} are same tree : {res}")

def test_string_nums():
    test_cases = [
        { "p": "[1,2,3]"       , "q": "[1,2,3]" },
        { "p": "[1,2]"         , "q": "[1,null,2]" },
        { "p": "[1,2,1]"       , "q": "[1,1,2]" },
        { "p": "[1,2,5,6,9,10]", "q": "[1,2,5,6,9,10]"}
    ]
    sol = Solution()
    print("\n\n ----- [Test String Numbers] -----")
    for i, test_case in enumerate(test_cases, 1):
        p = sol.string_to_treenode(test_case["p"])
        q = sol.string_to_treenode(test_case["q"])
        res = sol.is_sametree(p, q)
        print(f"{i}. {test_case} are same tree : {res}")


if __name__ == '__main__':
    test_int_nums()
    test_string_nums()


