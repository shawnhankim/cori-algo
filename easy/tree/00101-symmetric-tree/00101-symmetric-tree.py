"""
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 
    
        1
     2     2
   3  4   4  3
 4 5 6 7 7 6 5 4   

Note:
Bonus points if you could solve it both recursively and iteratively.

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative Solution
class Solution(object):
    def is_symmetric(self, root):
        if not root:
            return True
        q = deque()
        q.append(root.left)
        q.append(root.right)
        res = True
        while q:
            l = q.popleft()
            r = q.popleft()
            if (not l and r) or (l and not r) or (l and r and l.val != r.val):
                res = False
                break
            if l:
                q.append(l.left)
                q.append(r.right)
            if r:
                q.append(l.right)
                q.append(r.left) 
               
        while q:
            q.pop()
        return res

# Recursive Solution
class Solution1(object):
    def is_symmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, l, r):
        if not l and not r:
            return True
        if (not l and r) or (l and not r) or (l.val != r.val):
            return False
        return self.helper(l.left, r.right) and self.helper(l.right, r.left)

from collections import deque
class Test(object):
    def assert_symmetric(self):
        test_cases = [
            [1, 2, 2],
            [1, 2, 2, 3, 4, 4, 3],
            [1, 2, 2, None, 3, None, 3],
            [1],
            [1, 2],
            [1, 2, 2, 3, 4, 4, 3, 4, 5, 6, 7, 7, 6, 5, 4],
            [1, 2, 2, 3, 4, 4, 3, 4, 5, 6, 7, 7, 6, 3, 4]
        ]
        for i, test_case in enumerate(test_cases, 1):
            root = self.list_to_tree(test_case)
            res  = Solution().is_symmetric(root)
            print(f"{i}. is tree? {res} for {test_case}") 

    def list_to_tree(self, nums):
        if not nums:
            return None
        i = 0
        root = TreeNode(nums[i])
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            i += 1
            if i < len(nums) and nums[i]:
                node.left = TreeNode(nums[i])    
                q.append(node.left)

            i += 1
            if i < len(nums) and nums[i]:
                node.right = TreeNode(nums[i])
                q.append(node.right)
        return root

    def helper(self, root, nums, i):
        if i >= len(nums):
            return None
        if nums[i]:
            root = TreeNode(nums[i])
            root.val = nums[i]
            root.left = self.helper(root, nums, i+1)
            root.right = self.helper(root, nums, i+2)
        return root


def main():
    Test().assert_symmetric()

if __name__ == '__main__':
    main()

